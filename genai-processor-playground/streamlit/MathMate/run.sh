#!/bin/bash

# MathMate Streamlit App Launch Script
# Enhanced with research capabilities

echo "🧮 Starting MathMate - Your AI Mathematics Companion with Research Capabilities"
echo "=============================================================================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please create a virtual environment first:"
    echo "python3 -m venv .venv"
    echo "source .venv/bin/activate"
    echo "pip install -r requirements.txt"
    exit 1
fi

# Use the virtual environment Python
PYTHON_PATH=".venv/bin/python"

# Check if Python exists in venv
if [ ! -f "$PYTHON_PATH" ]; then
    echo "❌ Python not found in virtual environment at $PYTHON_PATH"
    exit 1
fi

# Check if GOOGLE_API_KEY is set
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  Warning: GOOGLE_API_KEY environment variable is not set."
    echo "Please set your Google AI Studio API key:"
    echo "export GOOGLE_API_KEY='your-api-key-here'"
    echo ""
    echo "The app will show an error until the API key is configured."
    echo ""
fi

# Check if streamlit is installed
if ! $PYTHON_PATH -c "import streamlit" 2>/dev/null; then
    echo "❌ Streamlit not found. Installing dependencies..."
    $PYTHON_PATH -m pip install -r requirements.txt
fi

# Check if genai-processors is installed with research support
if ! $PYTHON_PATH -c "from genai_processors.examples import research" 2>/dev/null; then
    echo "⚠️  Research functionality may not be available."
    echo "To enable full research capabilities, ensure genai-processors is properly installed."
fi

echo ""
echo "🚀 Launching MathMate with research capabilities..."
echo "💬 Chat Mode: Interactive mathematics assistant"
echo "🔬 Research Mode: In-depth mathematical research and analysis"
echo ""
echo "Access the app at: http://localhost:8501"
echo "Press Ctrl+C to stop the application"
echo ""

# Launch the Streamlit app using the virtual environment Python
$PYTHON_PATH -m streamlit run app.py --server.port 8501 --server.address localhost
