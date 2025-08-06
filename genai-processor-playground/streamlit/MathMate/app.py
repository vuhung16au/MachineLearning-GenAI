# Copyright 2025 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Streamlit-based MathMate chat application with Gemini model.

Features:
- Web UI: Streamlit interface for interactive conversation
- Text-based chat: Interactive conversation with Gemini
- Multimodal support: Can process URLs for images and PDFs
- Context management: Maintains conversation history
- Error handling: Proper validation and exception handling
- Google Search integration: Model has access to search tools

## Setup

To install the dependencies for this script, run:

```
pip install --upgrade genai-processors google-genai streamlit httpx
```

Before running this script, ensure the `GOOGLE_API_KEY` environment
variable is set.

## Run

To run the Streamlit app:

```shell
streamlit run app.py
```
"""

import asyncio
import dataclasses
import os
import sys
from typing import AsyncIterable, AsyncGenerator, List
import traceback

import streamlit as st
from genai_processors import content_api
from genai_processors import context
from genai_processors import processor
from genai_processors import streams
from genai_processors.core import pdf
from genai_processors.core import realtime
from genai_processors.core import text
import httpx

# Try to import research functionality
try:
    from genai_processors.examples import research
    RESEARCH_AVAILABLE = True
except ImportError:
    RESEARCH_AVAILABLE = False
    st.warning("Research functionality not available. Install genai-processors with research examples.")

# Import configuration
import config


@dataclasses.dataclass(frozen=True)
class FetchRequest:
    """A request to fetch content from a URL."""
    url: str


class _FetchUrl(processor.PartProcessor):
    """A PartProcessor that fetches the content for a given URL.

    DO NOT USE OUTSIDE OF THIS EXAMPLE: NOT PRODUCTION QUALITY.

    This is an oversimplified version of FetchUrl to allow testing multimodal
    content handling (images, PDFs). It will be replaced with a proper version
    from core.web once it is available.
    """

    def match(self, part: content_api.ProcessorPart) -> bool:
        """This processor matches on WebRequest parts."""
        return content_api.is_dataclass(part.mimetype, FetchRequest)

    @processor.yield_exceptions_as_parts
    async def call(
        self, part: content_api.ProcessorPart
    ) -> AsyncIterable[content_api.ProcessorPart]:
        """Gets the content for a given URL."""
        webrequest = part.get_dataclass(FetchRequest)
        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(webrequest.url)
            response.raise_for_status()

        yield content_api.ProcessorPart(
            response.content, mimetype=response.headers.get('content-type')
        )


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'research_results' not in st.session_state:
        st.session_state.research_results = None
    if 'research_in_progress' not in st.session_state:
        st.session_state.research_in_progress = False
    if 'generated_topics' not in st.session_state:
        st.session_state.generated_topics = []
    if 'status_updates' not in st.session_state:
        st.session_state.status_updates = []
    if 'current_mode' not in st.session_state:
        st.session_state.current_mode = 'chat'  # 'chat' or 'research'
    if 'chat_agent' not in st.session_state:
        try:
            # Create the main model processor directly without using flags
            from genai_processors.core import genai_model
            from google.genai import types as genai_types
            
            if not config.GOOGLE_API_KEY:
                raise ValueError("Google API key is not set")
            
            model = genai_model.GenaiModel(
                api_key=config.GOOGLE_API_KEY,
                model_name=config.DEFAULT_MODEL_NAME,
                generate_content_config=genai_types.GenerateContentConfig(
                    system_instruction=config.SYSTEM_INSTRUCTION[0],  # Use the first string
                    response_modalities=['TEXT'],
                    # Adds google search as a tool
                    tools=[genai_types.Tool(google_search=genai_types.GoogleSearch())],
                ),
                # Make the newest features available
                http_options=genai_types.HttpOptions(api_version='v1alpha'),
            )
            
            # Create a live model processor that maintains conversation context
            chat_agent = realtime.LiveModelProcessor(model)
            
            # Add multimodal capabilities: URL extraction and content fetching
            https_extractor = text.UrlExtractor({'https://': FetchRequest})
            http_extractor = text.UrlExtractor({'http://': FetchRequest})
            
            st.session_state.chat_agent = (
                https_extractor 
                + http_extractor
                + _FetchUrl() 
                + pdf.PDFExtract() 
                + chat_agent
            )
        except Exception as e:
            st.error(f"Failed to initialize chat agent: {str(e)}")
            st.session_state.chat_agent = None


async def process_user_input(user_input: str):
    """Process user input and return the complete response."""
    if not st.session_state.chat_agent:
        return config.INIT_ERROR
    
    try:
        # Create an async generator for the user input
        async def input_generator():
            yield content_api.ProcessorPart(user_input)
        
        response_text = ""
        async for part in st.session_state.chat_agent(input_generator()):
            # Filter out status messages and reserved substreams
            if context.is_reserved_substream(part.substream_name):
                continue
            
            if part.text:
                response_text += part.text
        
        return response_text if response_text else config.RESPONSE_ERROR
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"


def run_async(coro):
    """Run an async coroutine in a sync context."""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    return loop.run_until_complete(coro)


def main():
    """Main Streamlit application."""
    st.set_page_config(
        page_title=config.APP_TITLE,
        page_icon=config.PAGE_ICON,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Check for API key
    if not config.GOOGLE_API_KEY:
        st.error(config.API_KEY_ERROR)
        st.info(config.API_KEY_INFO)
        st.code(config.API_KEY_EXAMPLE)
        return
    
    # Initialize session state
    initialize_session_state()
    
    # Main header
    st.title(config.APP_TITLE)
    st.subheader(config.APP_SUBTITLE)
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About MathMate")
        st.markdown("""
        **MathMate** is an AI assistant specialized in mathematics and problem-solving.
        
        **Features:**
        - 📚 Help with math concepts from basic to advanced
        - 🔗 Process URLs with mathematical content
        - 📄 Analyze PDFs and images
        - 🔍 Google Search integration
        - 💬 Conversation history
        
        **Examples:**
        - "What is the derivative of x²?"
        - "Explain this diagram: https://upload.wikimedia.org/wikipedia/commons/9/9b/Social_Network_Analysis_Visualization.png"
        - "Summarize this paper: https://arxiv.org/pdf/2303.08774"
        """)
        
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me any math question or share a URL..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # Show thinking indicator
            with st.spinner("🤔 Thinking..."):
                try:
                    # Process the input asynchronously
                    response = run_async(process_user_input(prompt))
                    
                    message_placeholder.markdown(response)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": response
                    })
                        
                except Exception as e:
                    error_msg = f"❌ An error occurred: {str(e)}"
                    message_placeholder.markdown(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": error_msg
                    })


if __name__ == "__main__":
    main()
