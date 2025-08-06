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
    research = None  # Set to None when not available

# Import configuration
import config
import re


@dataclasses.dataclass(frozen=True)
class FetchRequest:
    """A request to fetch content from a URL."""
    url: str


class UrlSummarizationProcessor(processor.PartProcessor):
    """A processor that handles URL summarization requests."""
    
    def match(self, part: content_api.ProcessorPart) -> bool:
        """Match text that contains URL summarization requests."""
        if not part.text:
            return False
        
        # Check for summarization patterns
        summarization_patterns = [
            r'summarise\s+this\s+url:\s*(https?://\S+)',
            r'summarize\s+this\s+url:\s*(https?://\S+)',
            r'summarise\s+url:\s*(https?://\S+)',
            r'summarize\s+url:\s*(https?://\S+)',
            r'summary\s+of\s*(https?://\S+)',
            r'summarise\s*(https?://\S+)',
            r'summarize\s*(https?://\S+)'
        ]
        
        text = part.text.lower()
        for pattern in summarization_patterns:
            if re.search(pattern, text):
                return True
        return False
    
    @processor.yield_exceptions_as_parts
    async def call(
        self, part: content_api.ProcessorPart
    ) -> AsyncIterable[content_api.ProcessorPart]:
        """Process URL summarization requests."""
        text = part.text
        
        # Extract URL from the request
        url_patterns = [
            r'summarise\s+this\s+url:\s*(https?://\S+)',
            r'summarize\s+this\s+url:\s*(https?://\S+)',
            r'summarise\s+url:\s*(https?://\S+)',
            r'summarize\s+url:\s*(https?://\S+)',
            r'summary\s+of\s*(https?://\S+)',
            r'summarise\s*(https?://\S+)',
            r'summarize\s*(https?://\S+)'
        ]
        
        url = None
        for pattern in url_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                url = match.group(1)
                break
        
        if url:
            # Instead of creating a FetchRequest, just pass the URL as text
            # The existing URL extractors will handle it
            yield content_api.ProcessorPart(
                f"Please fetch and summarize the content from this URL: {url}. "
                f"Provide a comprehensive summary focusing on the main points and key information. "
                f"Structure your response as 'Summary of {url}:' followed by the summary.",
                mimetype='text/plain'
            )
        else:
            yield content_api.ProcessorPart(
                "I couldn't find a valid URL in your request. Please provide a URL to summarize.",
                mimetype='text/plain'
            )


class _FetchUrl(processor.PartProcessor):
    """A PartProcessor that fetches the content for a given URL.

    Enhanced version with better error handling and content type detection.
    """

    def match(self, part: content_api.ProcessorPart) -> bool:
        """This processor matches on WebRequest parts."""
        return content_api.is_dataclass(part.mimetype, FetchRequest)

    @processor.yield_exceptions_as_parts
    async def call(
        self, part: content_api.ProcessorPart
    ) -> AsyncIterable[content_api.ProcessorPart]:
        """Gets the content for a given URL with enhanced error handling."""
        webrequest = part.get_dataclass(FetchRequest)
        url = webrequest.url
        
        try:
            # Set timeout and user agent for better compatibility
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; MathMate/1.0; +https://github.com/google-deepmind/genai-processors)'
            }
            
            async with httpx.AsyncClient(
                follow_redirects=True, 
                timeout=30.0,
                headers=headers
            ) as client:
                response = await client.get(url)
                response.raise_for_status()
                
                # Get content type
                content_type = response.headers.get('content-type', 'text/plain')
                
                # Handle different content types
                if 'text/html' in content_type:
                    # For HTML content, we'll pass it as text for the AI to process
                    yield content_api.ProcessorPart(
                        response.text, 
                        mimetype='text/plain'
                    )
                elif 'application/pdf' in content_type:
                    # PDF content will be handled by PDFExtract processor
                    yield content_api.ProcessorPart(
                        response.content, 
                        mimetype=content_type
                    )
                elif any(img_type in content_type for img_type in ['image/jpeg', 'image/png', 'image/gif', 'image/webp']):
                    # Image content
                    yield content_api.ProcessorPart(
                        response.content, 
                        mimetype=content_type
                    )
                else:
                    # Default to text processing
                    yield content_api.ProcessorPart(
                        response.text, 
                        mimetype='text/plain'
                    )
                    
        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            error_msg = f"HTTP {e.response.status_code}: Failed to fetch URL {url}"
            yield content_api.ProcessorPart(
                error_msg, 
                mimetype='text/plain'
            )
        except httpx.RequestError as e:
            # Handle network errors
            error_msg = f"Network error: Failed to fetch URL {url}. Error: {str(e)}"
            yield content_api.ProcessorPart(
                error_msg, 
                mimetype='text/plain'
            )
        except Exception as e:
            # Handle other errors
            error_msg = f"Unexpected error fetching URL {url}: {str(e)}"
            yield content_api.ProcessorPart(
                error_msg, 
                mimetype='text/plain'
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
            
            # Add URL summarization processor
            url_summarizer = UrlSummarizationProcessor()
            
            st.session_state.chat_agent = (
                url_summarizer
                + https_extractor 
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


def validate_api_key(api_key: str) -> bool:
    """Validate the Google API key."""
    if not api_key:
        return False
    # Basic validation - should start with specific pattern
    return api_key.startswith('AIza') and len(api_key) > 20


async def run_research_agent(api_key: str, user_prompt: str, research_config):
    """Run the research agent and yield results."""
    if not RESEARCH_AVAILABLE or research is None:
        yield {'type': 'error', 'content': 'Research functionality is not available. Please install genai-processors with research examples.'}
        return
        
    try:
        agent = research.ResearchAgent(api_key=api_key, config=research_config)
        input_stream = streams.stream_content([processor.ProcessorPart(user_prompt)])
        
        output_parts = content_api.ProcessorContent()
        async for content_part in agent(input_stream):
            if content_part.substream_name == 'status':
                yield {'type': 'status', 'content': content_part.text}
            else:
                output_parts += content_part
        
        # Final synthesized research
        final_research = content_api.as_text(output_parts, substream_name='')
        yield {'type': 'final', 'content': final_research}
        
    except Exception as e:
        yield {'type': 'error', 'content': f"Error running research agent: {str(e)}"}


async def generate_topics_only(api_key: str, user_prompt: str, research_config):
    """Generate topics without doing the full research."""
    if not RESEARCH_AVAILABLE or research is None:
        yield {'type': 'error', 'content': 'Research functionality is not available. Please install genai-processors with research examples.'}
        return
        
    try:
        p_generator = research.TopicGenerator(api_key=api_key, config=research_config)
        input_stream = streams.stream_content([processor.ProcessorPart(user_prompt)])
        
        topics = []
        async for content_part in p_generator(input_stream):
            if content_part.mimetype == 'application/json; type=Topic':
                topic_data = content_part.get_dataclass(research.interfaces.Topic)
                topics.append(topic_data)
            elif content_part.substream_name == 'status':
                yield {'type': 'status', 'content': content_part.text}
        
        yield {'type': 'topics', 'content': topics}
        
    except Exception as e:
        yield {'type': 'error', 'content': f"Error generating topics: {str(e)}"}


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
    
    # Mode selection tabs
    tab1, tab2 = st.tabs(["💬 Chat Mode", "🔬 Research Mode"])
    
    with tab1:
        chat_mode()
    
    with tab2:
        if RESEARCH_AVAILABLE:
            research_mode()
        else:
            st.error("🔬 Research mode is not available.")
            st.info("To enable research mode, please ensure the genai-processors library is installed with research examples.")
            st.code("pip install genai-processors[research]")
    
    # Footer
    st.divider()
    st.markdown(
        "Built with [Streamlit](https://streamlit.io) • "
        "Powered by [GenAI Processors](https://github.com/google-deepmind/genai-processors) • "
        "🧮 MathMate - Your AI Mathematics Companion"
    )


def chat_mode():
    """Handle the chat mode interface."""
    # Sidebar with information
    with st.sidebar:
        st.header("💬 Chat Features")
        st.markdown("""
        **MathMate Chat** is an AI assistant specialized in mathematics and problem-solving.
        
        **Features:**
        - 📚 Help with math concepts from basic to advanced
        - 🔗 Process URLs with mathematical content
        - 📄 Analyze PDFs and images
        - 🔍 Google Search integration
        - 💬 Conversation history
        - 📋 URL summarization capabilities
        
        **Examples:**
        - "What is the derivative of x²?"
        - "Summarise this URL: https://en.wikipedia.org/wiki/Australia"
        - "Explain this diagram: https://upload.wikimedia.org/wikipedia/commons/9/9b/Social_Network_Analysis_Visualization.png"
        - "Summarize this paper: https://arxiv.org/pdf/2303.08774"
        """)
        
        if st.button("Clear Chat History", key="clear_chat"):
            st.session_state.messages = []
            st.rerun()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me any math question, summarize a URL, or share content..."):
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


def research_mode():
    """Handle the research mode interface."""
    # Sidebar for research configuration
    with st.sidebar:
        st.header("🔬 Research Settings")
        
        # Research configuration
        num_topics = st.slider(
            "Number of Topics",
            min_value=1,
            max_value=10,
            value=config.DEFAULT_NUM_TOPICS,
            help="Number of research topics to generate"
        )
        
        model_name = st.selectbox(
            "Model",
            options=config.AVAILABLE_MODELS,
            index=0,
            help="AI model to use for research"
        )
        
        excluded_topics = st.text_area(
            "Excluded Topics (optional)",
            placeholder="Enter topics to exclude, one per line",
            help="Topics that should not be researched"
        )
        
        # Process excluded topics
        excluded_list = None
        if excluded_topics.strip():
            excluded_list = [topic.strip() for topic in excluded_topics.split('\n') if topic.strip()]
        
        st.divider()
        st.markdown("""
        **Research Features:**
        
        1. **Generates Topics** - Creates relevant research topics based on your query
        2. **Researches Each Topic** - Uses AI and web search to gather information
        3. **Synthesizes Results** - Combines findings into a comprehensive report
        
        Perfect for mathematical research, concept exploration, and in-depth analysis.
        """)
    
    # Main research content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Research Query")
        
        # Example prompts for research
        selected_example = st.selectbox(
            "Choose an example or write your own:",
            options=["Custom"] + config.EXAMPLE_RESEARCH_PROMPTS,
            index=0
        )
        
        if selected_example != "Custom":
            default_prompt = selected_example
        else:
            default_prompt = ""
        
        user_prompt = st.text_area(
            "Research Topic",
            value=default_prompt,
            height=100,
            placeholder="Enter what you'd like to research...",
            help="Describe the mathematical topic you want to research in detail"
        )
        
        # Action buttons
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            preview_topics = st.button(
                "🔍 Preview Topics",
                disabled=not user_prompt.strip(),
                help="Generate topics without full research"
            )
        
        with col_btn2:
            start_research = st.button(
                "🚀 Start Research",
                disabled=not user_prompt.strip() or st.session_state.research_in_progress,
                help="Begin full research process"
            )
        
        with col_btn3:
            if st.session_state.research_in_progress:
                st.button("⏹️ Research in Progress...", disabled=True)
    
    with col2:
        st.header("ℹ️ Research Info")
        st.markdown("""
        **Mathematical Research Agent:**
        
        - 🎯 **Topic Generation**: Identifies key areas to explore
        - 🔍 **Deep Research**: Uses web search and AI analysis
        - 📊 **Synthesis**: Combines findings into comprehensive reports
        - 🧮 **Math Focus**: Specialized for mathematical content
        """)
        
        if st.button("Clear Research Results", key="clear_research"):
            st.session_state.research_results = None
            st.session_state.generated_topics = []
            st.session_state.status_updates = []
            st.rerun()
    
    # Create research configuration object
    if RESEARCH_AVAILABLE and research is not None:
        research_config = research.interfaces.Config(
            topic_generator_model_name=model_name,
            topic_researcher_model_name=model_name,
            research_synthesizer_model_name=model_name,
            num_topics=num_topics,
            excluded_topics=excluded_list
        )
    else:
        research_config = None
    
    # Handle topic preview
    if preview_topics and research_config and config.GOOGLE_API_KEY:
        with st.spinner("Generating topics..."):
            try:
                # Run topic generation
                async def run_topic_generation():
                    api_key = config.GOOGLE_API_KEY
                    if not api_key:
                        return [{'type': 'error', 'content': 'API key not available'}]
                    results = []
                    async for result in generate_topics_only(api_key, user_prompt, research_config):
                        results.append(result)
                    return results
                
                results = run_async(run_topic_generation())
                
                # Process results
                for result in results:
                    if result['type'] == 'status':
                        st.info(f"Status: {result['content']}")
                    elif result['type'] == 'topics':
                        st.session_state.generated_topics = result['content']
                    elif result['type'] == 'error':
                        st.error(result['content'])
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    # Display generated topics
    if st.session_state.generated_topics:
        st.header("📋 Generated Topics")
        
        for i, topic in enumerate(st.session_state.generated_topics, 1):
            # Handle both Topic dataclass and string formats
            topic_title = getattr(topic, 'topic', str(topic))
            topic_relation = getattr(topic, 'relationship_to_user_content', 'Auto-generated topic')
            
            with st.expander(f"Topic {i}: {topic_title}", expanded=True):
                st.write(f"**Relationship to query:** {topic_relation}")
    
    # Handle full research
    if start_research and research_config and config.GOOGLE_API_KEY:
        st.session_state.research_in_progress = True
        st.session_state.status_updates = []
        st.session_state.research_results = None
        
        # Create containers for real-time updates
        status_container = st.container()
        progress_bar = st.progress(0)
        
        try:
            # Run research agent
            async def run_research():
                api_key = config.GOOGLE_API_KEY
                if not api_key:
                    return [{'type': 'error', 'content': 'API key not available'}]
                results = []
                async for result in run_research_agent(api_key, user_prompt, research_config):
                    results.append(result)
                return results
            
            with st.spinner("Running research agent..."):
                results = run_async(run_research())
            
            # Process results
            status_count = 0
            total_expected_status = 10  # Rough estimate
            
            for result in results:
                if result['type'] == 'status':
                    status_count += 1
                    st.session_state.status_updates.append(result['content'])
                    progress_bar.progress(min(status_count / total_expected_status, 0.9))
                    
                    with status_container:
                        st.info(f"📄 {result['content']}")
                
                elif result['type'] == 'final':
                    st.session_state.research_results = result['content']
                    progress_bar.progress(1.0)
                
                elif result['type'] == 'error':
                    st.error(result['content'])
                    break
            
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
            st.error("Full error details:")
            st.code(traceback.format_exc())
        
        finally:
            st.session_state.research_in_progress = False
    
    # Display research results
    if st.session_state.research_results:
        st.header("📊 Research Results")
        
        # Add download button
        st.download_button(
            label="📥 Download Research Report",
            data=st.session_state.research_results,
            file_name=f"mathmate_research_{user_prompt[:30].replace(' ', '_')}.md",
            mime="text/markdown"
        )
        
        # Display the research
        st.markdown(st.session_state.research_results)
    
    # Display status history
    if st.session_state.status_updates:
        with st.expander("📜 Research Process Log", expanded=False):
            for i, status in enumerate(st.session_state.status_updates, 1):
                st.text(f"{i}. {status}")


if __name__ == "__main__":
    main()
