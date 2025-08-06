# 🧮 MathMate - Streamlit Chat Application

A Streamlit-based chat application featuring MathMate, an AI assistant specialized in mathematics and problem-solving powered by Google's Gemini model.

## Features

- **Web UI**: Interactive Streamlit interface for seamless conversation
- **Mathematical Expertise**: Help with concepts from basic arithmetic to advanced topics
- **Multimodal Support**: Process URLs for images and PDFs
- **Context Management**: Maintains conversation history throughout the session
- **Google Search Integration**: Model has access to search tools for enhanced responses
- **Error Handling**: Proper validation and exception handling

## Prerequisites

Before running this application, ensure you have:

1. **Python 3.8+** installed
2. **Google API Key** from [AI Studio](https://aistudio.google.com/)

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variable**
   ```bash
   export GOOGLE_API_KEY='your-api-key-here'
   ```
   
   Or create a `.env` file in the project directory:
   ```
   GOOGLE_API_KEY=your-api-key-here
   ```

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Using MathMate

1. **Basic Math Questions**
   - "What is the derivative of x²?"
   - "Explain the Pythagorean theorem"
   - "How do I solve quadratic equations?"

2. **URL Analysis**
   - "Explain this diagram: https://example.com/math-diagram.png"
   - "Summarize this paper: https://arxiv.org/pdf/math-paper.pdf"

3. **Advanced Topics**
   - "Explain calculus concepts"
   - "Help me with linear algebra"
   - "Statistics and probability questions"

## Application Structure

```
TurnBasedChat/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Key Components

### Chat Interface
- **Message History**: All conversations are preserved during the session
- **Real-time Responses**: Streaming responses from the AI model
- **Error Handling**: Graceful handling of API errors and network issues

### Multimodal Processing
- **URL Extraction**: Automatically detects and processes HTTP/HTTPS URLs
- **PDF Processing**: Extracts and analyzes content from PDF documents
- **Image Analysis**: Processes mathematical diagrams and visual content

### AI Model Integration
- **Gemini Integration**: Uses Google's Gemini model for mathematical reasoning
- **System Instructions**: Specialized prompts for mathematical assistance
- **Search Tools**: Access to Google Search for enhanced knowledge

## Troubleshooting

### Common Issues

1. **"GOOGLE_API_KEY environment variable is not set"**
   - Ensure your API key is properly set in environment variables
   - Check that the key is valid and has appropriate permissions

2. **"Chat agent is not initialized"**
   - Verify your API key is correct
   - Check your internet connection
   - Ensure all dependencies are installed

3. **Import Errors**
   - Run `pip install -r requirements.txt` to install all dependencies
   - Ensure you're using Python 3.8 or higher

### Performance Tips

- For better performance, use a stable internet connection
- Large PDFs or complex images may take longer to process
- Clear chat history periodically for optimal performance

## Comparison with CLI Version

This Streamlit app provides the same core functionality as the original CLI version (`turn_based_chat.py`) with these enhancements:

- **Web Interface**: User-friendly browser-based interface
- **Visual Chat History**: Persistent message display
- **Better Error Handling**: Visual error messages and status indicators
- **Responsive Design**: Works on desktop and mobile devices
- **Session Management**: Automatic state preservation

## Development

To extend or modify the application:

1. **Add New Features**: Modify `app.py` to add new Streamlit components
2. **Customize UI**: Use Streamlit's theming and CSS capabilities
3. **Extend Processing**: Add new processors to the pipeline for additional file types


