# Research Agent Configuration
# This file contains default configuration options for the Research Agent Streamlit app.
# You can modify these values to customize the default behavior.
#
# Licensed under the MIT License. See LICENSE.md for more information.

# Default Models
DEFAULT_TOPIC_GENERATOR_MODEL = "gemini-2.5-flash"
DEFAULT_TOPIC_RESEARCHER_MODEL = "gemini-2.5-flash"
DEFAULT_RESEARCH_SYNTHESIZER_MODEL = "gemini-2.5-flash"

# Research Parameters
DEFAULT_NUM_TOPICS = 5
MAX_TOPICS = 10
MIN_TOPICS = 1

# UI Configuration
APP_TITLE = "🔬 Research Agent"
APP_ICON = "🔬"

# Example Research Prompts
EXAMPLE_PROMPTS = [
    "Research the best things about Australia's military power!",
    "What are the latest developments in artificial intelligence?",
    "How can I start a vegetable garden in a small urban space?",
    "What are the environmental impacts of renewable energy?",
    "Best practices for remote team management",
    "Latest trends in sustainable architecture",
    "Impact of social media on mental health",
    "Blockchain technology applications beyond cryptocurrency",
    "Future of electric vehicles and charging infrastructure",
    "Benefits and challenges of remote work for productivity"
]

# Available Models
AVAILABLE_MODELS = [
    "gemini-2.5-flash",
    "gemini-1.5-pro", 
    "gemini-1.5-flash"
]

# Status Messages
STATUS_MESSAGES = {
    "generating_topics": "🔍 Generating research topics...",
    "researching": "📚 Researching topics...",
    "synthesizing": "✍️ Synthesizing research results...",
    "complete": "✅ Research complete!",
    "error": "❌ An error occurred during research."
}

# Help Text
HELP_TEXT = {
    "api_key": "Enter your Google AI Studio API key. Get one at https://aistudio.google.com/",
    "num_topics": "Number of research topics to generate and research",
    "model": "AI model to use for research. Flash models are faster, Pro models are more comprehensive",
    "excluded_topics": "Topics that should not be researched, one per line",
    "research_query": "Describe what you want to research in detail for best results"
}

# Advanced Configuration
RESEARCH_CONFIG = {
    "max_retries": 3,
    "timeout_seconds": 300,
    "enable_web_search": True,
    "max_status_updates": 50
}
