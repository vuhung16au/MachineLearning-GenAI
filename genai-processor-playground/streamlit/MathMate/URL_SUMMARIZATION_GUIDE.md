# URL Summarization Guide for MathMate

## Overview

MathMate now includes enhanced URL summarization capabilities that allow users to request summaries of web content, PDFs, and images. This functionality is built using only the libraries specified in `requirements.txt`.

## Features

### Supported Content Types
- **Web Pages**: HTML content from websites
- **PDF Documents**: Academic papers, reports, and documents
- **Images**: Mathematical diagrams, charts, and visual content
- **Text Documents**: Plain text and formatted content

### Supported URL Formats
- HTTP URLs: `http://example.com`
- HTTPS URLs: `https://example.com`
- PDF URLs: `https://arxiv.org/pdf/2303.08774`
- Image URLs: `https://upload.wikimedia.org/wikipedia/commons/...`

## Usage Examples

### Basic URL Summarization
```
Summarise this URL: https://en.wikipedia.org/wiki/Australia
```

### Alternative Formats
```
Summarize this URL: https://example.com
Summarise URL: https://mathworld.wolfram.com/
Summary of https://arxiv.org/abs/2303.08774
```

### Mathematical Content
```
Summarise this mathematical paper: https://arxiv.org/pdf/2303.08774
Explain this diagram: https://upload.wikimedia.org/wikipedia/commons/9/9b/Social_Network_Analysis_Visualization.png
```

## How It Works

### 1. URL Detection
The system uses regex patterns to detect summarization requests:
- `summarise this url: [URL]`
- `summarize this url: [URL]`
- `summarise url: [URL]`
- `summary of [URL]`
- And variations with different spellings

### 2. Content Fetching
- **Enhanced HTTP Client**: Uses `httpx` with proper headers and timeout
- **Error Handling**: Comprehensive error handling for network issues
- **Content Type Detection**: Automatically detects and handles different content types
- **Redirect Support**: Follows redirects automatically

### 3. Content Processing
- **HTML Content**: Converted to text for AI processing
- **PDF Content**: Handled by the PDF extraction processor
- **Image Content**: Processed as visual content
- **Text Content**: Directly processed

### 4. AI Summarization
- **Comprehensive Summaries**: Focuses on main points and key information
- **Mathematical Focus**: Prioritizes mathematical content when present
- **Structured Output**: Returns summaries in a consistent format

## Technical Implementation

### Core Components

#### 1. UrlSummarizationProcessor
```python
class UrlSummarizationProcessor(processor.PartProcessor):
    """A processor that handles URL summarization requests."""
    
    def match(self, part: content_api.ProcessorPart) -> bool:
        # Detects summarization requests using regex patterns
    
    async def call(self, part: content_api.ProcessorPart):
        # Extracts URLs and generates summarization instructions
```

#### 2. Enhanced _FetchUrl Processor
```python
class _FetchUrl(processor.PartProcessor):
    """Enhanced URL fetching with better error handling."""
    
    async def call(self, part: content_api.ProcessorPart):
        # Fetches content with proper headers and error handling
        # Handles different content types appropriately
```

### Error Handling

The system handles various error scenarios:
- **HTTP Errors**: 404, 403, 500, etc.
- **Network Errors**: Connection timeouts, DNS failures
- **Content Errors**: Invalid content types, encoding issues
- **Timeout Errors**: 30-second timeout for requests

### Content Type Support

| Content Type | Processing Method | Output |
|-------------|------------------|---------|
| `text/html` | Converted to text | Text summary |
| `application/pdf` | PDF extraction | Text summary |
| `image/*` | Visual processing | Description + analysis |
| `text/plain` | Direct processing | Text summary |

## Configuration

### System Instructions
The AI model is configured with specific instructions for URL summarization:
- Fetch content from URLs when requested
- Provide comprehensive summaries
- Focus on mathematical content when present
- Structure responses consistently

### Processing Pipeline
```
UrlSummarizationProcessor → UrlExtractor → _FetchUrl → PDFExtract → ChatAgent
```

## Usage in the Application

### Chat Mode
1. Enter a summarization request in the chat input
2. The system automatically detects the request
3. Content is fetched and processed
4. A comprehensive summary is returned

### Example Interaction
```
User: Summarise this URL: https://en.wikipedia.org/wiki/Australia
MathMate: Summary of https://en.wikipedia.org/wiki/Australia:
Australia is a sovereign country comprising the mainland of the Australian continent...
[Comprehensive summary continues]
```

## Limitations

### Current Limitations
- **Rate Limiting**: Some websites may block rapid requests
- **JavaScript Content**: Dynamic content may not be captured
- **Authentication**: Protected content cannot be accessed
- **Large Files**: Very large PDFs may timeout

### Best Practices
- Use HTTPS URLs when possible
- Provide specific URLs rather than search queries
- For mathematical content, specify the type of analysis needed
- Be patient with large documents

## Testing

The functionality can be tested using the provided test script:
```bash
python test_url_summarization.py
```

This tests:
- URL pattern matching
- Request processing
- Error handling
- Different input formats

## Dependencies

All functionality uses only the libraries specified in `requirements.txt`:
- `genai_processors`: Core processing framework
- `google-genai`: AI model integration
- `streamlit`: Web interface
- `httpx`: HTTP client for URL fetching
- `termcolor`: Terminal output formatting
- `python-dotenv`: Environment variable management
- `asyncio`: Asynchronous programming support

## Future Enhancements

Potential improvements for future versions:
- **Caching**: Cache frequently requested URLs
- **Batch Processing**: Handle multiple URLs simultaneously
- **Advanced Parsing**: Better HTML structure understanding
- **Content Filtering**: Focus on specific content types
- **Export Options**: Save summaries in different formats
