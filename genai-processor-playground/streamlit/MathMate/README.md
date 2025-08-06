# 🧮 MathMate - AI Mathematics Companion with Research Capabilities

A comprehensive Streamlit-based application featuring MathMate, an AI assistant specialized in mathematics and problem-solving, now enhanced with powerful research capabilities powered by Google's Gemini model.

## Features

### 💬 Chat Mode
- **Interactive Conversations**: Real-time mathematical assistance
- **Mathematical Expertise**: Help with concepts from basic arithmetic to advanced topics
- **Multimodal Support**: Process URLs for images and PDFs
- **Context Management**: Maintains conversation history throughout the session
- **Google Search Integration**: Model has access to search tools for enhanced responses

### 🔬 Research Mode
- **Topic Generation**: Automatically generates relevant research topics based on your query
- **Deep Research**: Uses AI and web search to gather comprehensive information
- **Synthesis**: Combines findings into well-structured research reports
- **Configurable Parameters**: Adjust number of topics, models, and exclusions
- **Real-time Updates**: See the research process unfold with status updates
- **Export Functionality**: Download research reports as Markdown files

## Prerequisites

Before running this application, ensure you have:

1. **Python 3.8+** installed
2. **Google API Key** from [AI Studio](https://aistudio.google.com/)
3. **Virtual Environment** (recommended)

## Setup

1. **Create Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variable**
   ```bash
   export GOOGLE_API_KEY='your-api-key-here'
   ```
   
   Or create a `.env` file in the project directory:
   ```
   GOOGLE_API_KEY=your-api-key-here
   ```

## Usage

### Running the Application

**Option 1: Using the launch script (recommended)**
```bash
./run.sh
```

**Option 2: Direct command**
```bash
.venv/bin/python -m streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Using MathMate

#### 💬 Chat Mode Examples

1. **Basic Math Questions**
   - "What is the derivative of x²?"
   - "Explain the Pythagorean theorem"
   - "How do I solve quadratic equations?"

2. **URL Analysis**
   - "Explain this diagram: <https://example.com/math-diagram.png>"
   - "Summarize this paper: <https://arxiv.org/pdf/math-paper.pdf>"

3. **Advanced Topics**
   - "Explain calculus concepts"
   - "Help me with linear algebra"
   - "Statistics and probability questions"

#### 🔬 Research Mode Examples

1. **Mathematical Research Queries**
   - "Research the latest developments in quantum computing and its applications in mathematics"
   - "Investigate the mathematical foundations of machine learning algorithms"
   - "Study the applications of differential equations in physics and engineering"

2. **Research Process**
   - Click "Preview Topics" to see generated research topics
   - Click "Start Research" to begin comprehensive research
   - Watch real-time status updates as the agent works
   - Download the final research report as a Markdown file

3. **Configuration Options**
   - Adjust number of topics (1-10)
   - Choose different AI models
   - Exclude specific topics from research

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


