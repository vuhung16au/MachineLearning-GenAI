

"""
Streamlit Research Agent Application

This Streamlit app provides an interactive web interface for the Research Agent
that was originally demonstrated in the research_agent.py example. Users can
input research queries through a web interface and see the complete research
process unfold in real-time.

Features:
- Interactive web interface for research queries
- Real-time status updates showing the research process
- Configurable research parameters (number of topics, models, etc.)
- Visual display of generated topics before research
- Final synthesized research output
- Error handling and user-friendly feedback

Licensed under the MIT License. See LICENSE.md for more information.
"""

import asyncio
import os
import streamlit as st
from typing import List
import sys
import traceback

# Add the research module to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import configuration
try:
    from config import *
except ImportError:
    # Fallback configuration if config.py is missing
    DEFAULT_NUM_TOPICS = 5
    EXAMPLE_PROMPTS = ["Research the best things about Vietnam's military power!"]
    AVAILABLE_MODELS = ["gemini-2.5-flash", "gemini-1.5-pro", "gemini-1.5-flash"]

try:
    from genai_processors import content_api
    from genai_processors import processor
    from genai_processors import streams
    from genai_processors.examples import research
except ImportError as e:
    st.error(f"Import error: {e}")
    st.error("Please ensure the genai-processors library is properly installed.")
    st.error("Try running: pip install -r requirements.txt")
    st.stop()

ProcessorPart = processor.ProcessorPart


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'research_results' not in st.session_state:
        st.session_state.research_results = None
    if 'research_in_progress' not in st.session_state:
        st.session_state.research_in_progress = False
    if 'generated_topics' not in st.session_state:
        st.session_state.generated_topics = []
    if 'status_updates' not in st.session_state:
        st.session_state.status_updates = []


def validate_api_key(api_key: str) -> bool:
    """Validate the Google API key."""
    if not api_key:
        return False
    # Basic validation - should start with specific pattern
    return api_key.startswith('AIza') and len(api_key) > 20


async def run_research_agent(api_key: str, user_prompt: str, config: research.interfaces.Config):
    """Run the research agent and yield results."""
    try:
        agent = research.ResearchAgent(api_key=api_key, config=config)
        input_stream = streams.stream_content([ProcessorPart(user_prompt)])
        
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


async def generate_topics_only(api_key: str, user_prompt: str, config: research.interfaces.Config):
    """Generate topics without doing the full research."""
    try:
        p_generator = research.TopicGenerator(api_key=api_key, config=config)
        input_stream = streams.stream_content([ProcessorPart(user_prompt)])
        
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


def main():
    """Main Streamlit application."""
    st.set_page_config(
        page_title="Research Agent",
        page_icon="🔬",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    initialize_session_state()
    
    # Header
    st.title("🔬 Research Agent")
    st.markdown("*Powered by GenAI Processors - Automated research synthesis*")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Google API Key",
            type="password",
            help="Enter your Google AI Studio API key"
        )
        
        if api_key and not validate_api_key(api_key):
            st.warning("⚠️ API key format appears invalid")
        
        st.divider()
        
        # Research configuration
        st.subheader("Research Settings")
        
        num_topics = st.slider(
            "Number of Topics",
            min_value=1,
            max_value=10,
            value=DEFAULT_NUM_TOPICS,
            help="Number of research topics to generate"
        )
        
        model_name = st.selectbox(
            "Model",
            options=AVAILABLE_MODELS,
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
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Research Query")
        
        # Default example prompts
        example_prompts = EXAMPLE_PROMPTS
        
        selected_example = st.selectbox(
            "Choose an example or write your own:",
            options=["Custom"] + example_prompts,
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
            help="Describe the topic you want to research in detail"
        )
        
        # Action buttons
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            preview_topics = st.button(
                "🔍 Preview Topics",
                disabled=not (api_key and user_prompt.strip()),
                help="Generate topics without full research"
            )
        
        with col_btn2:
            start_research = st.button(
                "🚀 Start Research",
                disabled=not (api_key and user_prompt.strip()) or st.session_state.research_in_progress,
                help="Begin full research process"
            )
        
        with col_btn3:
            if st.session_state.research_in_progress:
                st.button("⏹️ Research in Progress...", disabled=True)
    
    with col2:
        st.header("ℹ️ About")
        st.markdown("""
        This Research Agent:
        
        1. **Generates Topics** - Creates relevant research topics based on your query
        2. **Researches Each Topic** - Uses AI and web search to gather information
        3. **Synthesizes Results** - Combines findings into a comprehensive report
        
        **Features:**
        - Real-time status updates
        - Configurable parameters
        - Topic preview
        - Web search integration
        """)
    
    # Create configuration object
    config = research.interfaces.Config(
        topic_generator_model_name=model_name,
        topic_researcher_model_name=model_name,
        research_synthesizer_model_name=model_name,
        num_topics=num_topics,
        excluded_topics=excluded_list
    )
    
    # Handle topic preview
    if preview_topics:
        if not validate_api_key(api_key):
            st.error("❌ Please enter a valid Google API key")
        else:
            with st.spinner("Generating topics..."):
                try:
                    # Run topic generation
                    async def run_topic_generation():
                        results = []
                        async for result in generate_topics_only(api_key, user_prompt, config):
                            results.append(result)
                        return results
                    
                    results = asyncio.run(run_topic_generation())
                    
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
            with st.expander(f"Topic {i}: {topic.topic}", expanded=True):
                st.write(f"**Relationship to query:** {topic.relationship_to_user_content}")
    
    # Handle full research
    if start_research:
        if not validate_api_key(api_key):
            st.error("❌ Please enter a valid Google API key")
        else:
            st.session_state.research_in_progress = True
            st.session_state.status_updates = []
            st.session_state.research_results = None
            
            # Create containers for real-time updates
            status_container = st.container()
            progress_bar = st.progress(0)
            
            try:
                # Run research agent
                async def run_research():
                    results = []
                    async for result in run_research_agent(api_key, user_prompt, config):
                        results.append(result)
                    return results
                
                with st.spinner("Running research agent..."):
                    results = asyncio.run(run_research())
                
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
            file_name=f"research_report_{user_prompt[:30].replace(' ', '_')}.md",
            mime="text/markdown"
        )
        
        # Display the research
        st.markdown(st.session_state.research_results)
    
    # Display status history
    if st.session_state.status_updates:
        with st.expander("📜 Process Log", expanded=False):
            for i, status in enumerate(st.session_state.status_updates, 1):
                st.text(f"{i}. {status}")
    
    # Footer
    st.divider()
    st.markdown(
        "Built with [Streamlit](https://streamlit.io) • "
        "Powered by [GenAI Processors](https://github.com/google-deepmind/genai-processors) • "
    )


if __name__ == "__main__":
    main()
