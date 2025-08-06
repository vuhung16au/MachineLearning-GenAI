#!/bin/bash

# MathMate Streamlit App Startup Script

echo "🧮 Starting MathMate Streamlit Application..."

# Check if API key is set
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "❌ Warning: GOOGLE_API_KEY environment variable is not set."
    echo "Please set your Google AI Studio API key:"
    echo "export GOOGLE_API_KEY='your-api-key-here'"
    echo ""
    echo "You can also create a .env file with:"
    echo "GOOGLE_API_KEY=your-api-key-here"
    echo ""
fi

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed. Installing dependencies..."
    pip install -r requirements.txt
fi

# Start the Streamlit app
echo "🚀 Launching MathMate..."
streamlit run app.py
