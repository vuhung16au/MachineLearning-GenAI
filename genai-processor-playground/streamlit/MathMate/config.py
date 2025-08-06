"""Configuration settings for MathMate Streamlit app."""

import os

# Model configuration
DEFAULT_MODEL_NAME = "gemini-2.0-flash-lite"
MODEL_TYPE = "gemini"

# UI configuration
APP_TITLE = "🧮 MathMate"
APP_SUBTITLE = "Your AI Mathematics Companion"
PAGE_ICON = "🧮"

# System instruction for the AI model
SYSTEM_INSTRUCTION = [
    'You are MathMate, a helpful AI assistant specialized in mathematics and problem-solving. '
    'You can help with various mathematical concepts, from basic arithmetic to advanced topics like '
    'calculus, algebra, geometry, statistics, and more. You can also process images and documents '
    'that contain mathematical content. '
    
    'When provided with URLs, you can fetch and analyze the content. If a user asks you to summarize '
    'a URL (e.g., "Summarise this URL: https://example.com"), you should: '
    '1. Fetch the content from the URL using the available tools '
    '2. Provide a comprehensive summary of the content '
    '3. Focus on mathematical content if present, but summarize all relevant information '
    '4. Structure your response as "Summary of [URL]: [content summary]" '
    
    'Always provide clear, step-by-step explanations and be encouraging in your responses. '
    'If you need to search for additional information, feel free to use Google search. '
    'Keep your responses concise but thorough - aim for a few sentences to a paragraph maximum '
    'unless the user specifically asks for a detailed explanation.'
]

# Environment variables
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Research configuration
DEFAULT_NUM_TOPICS = 3
AVAILABLE_MODELS = ["gemini-2.0-flash-lite", "gemini-1.5-pro", "gemini-1.5-flash"]
EXAMPLE_RESEARCH_PROMPTS = [
    "Research the latest developments in quantum computing and its applications in mathematics",
    "Investigate the mathematical foundations of machine learning algorithms",
    "Study the applications of differential equations in physics and engineering",
    "Research the history and applications of the Fibonacci sequence",
    "Explore the mathematical concepts behind cryptography and cybersecurity"
]

# Error messages
API_KEY_ERROR = "❌ Error: GOOGLE_API_KEY environment variable is not set."
API_KEY_INFO = "Please set your Google AI Studio API key in your environment variables."
API_KEY_EXAMPLE = "export GOOGLE_API_KEY='your-api-key-here'"

INIT_ERROR = "❌ Chat agent is not initialized. Please check your API key."
RESPONSE_ERROR = "❌ No response received. Please try again."
