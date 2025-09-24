# Gemini 2.5 Flash Demo with google.genai

A comprehensive demonstration of Google's Gemini 2.5 Flash model capabilities using the modern `google.genai` library with multimodal inputs including text, images, PDFs, videos, and audio files.

## 📋 Overview

This project showcases the powerful multimodal capabilities of Google's Gemini 2.5 Flash model through a Jupyter notebook that demonstrates:

- **Text Processing**: Creative story generation and content analysis
- **Image Analysis**: Detailed image description and interpretation
- **PDF Processing**: Document summarization and content extraction
- **Video Analysis**: Direct video file upload and content understanding
- **Audio Processing**: Speech transcription and audio content analysis

The demo uses the modern `google.genai` library for enhanced performance and simplified API interactions, providing practical examples of how to integrate the Gemini API into your applications and handle various input types effectively.

## 🚀 Features

- **Modern API**: Uses the latest `google.genai` library for enhanced performance
- **Multimodal Input Support**: Text, images, PDFs, videos, and audio
- **Simplified Integration**: Clean, intuitive API with `Client()` pattern
- **File Processing**: Direct file upload with `client.files.upload()`
- **Binary Data Handling**: Efficient processing with `types.Part.from_bytes()`
- **Error Handling**: Robust error handling for various input types
- **Cross-Platform**: Works on Google Colab and local environments

## 🛠️ Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini
- FFmpeg (for video processing)
- Internet connection for downloading sample files

## 📦 Installation

### Option 1: Local Development (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Gemini
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   **On macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```
   
   **On Windows:**
   ```bash
   .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API key**
   
   Create a `.env.local` file in the LangGraph-Credentials directory:
   ```bash
   mkdir -p ~/Documents/LangGraph-Credentials
   echo "GOOGLE_API_KEY=your-api-key-here" > ~/Documents/LangGraph-Credentials/.env.local
   ```

### Option 2: Google Colab

1. Open the notebook in Google Colab
2. Run the setup cells to install dependencies
3. Add your API key as a Colab secret named `GOOGLE_API_KEY`

## 🔧 Configuration

### API Key Setup

The project supports two authentication methods:

**Local Development:**
- Create a `.env.local` file in `~/Documents/LangGraph-Credentials/` with your API key
- The notebook will automatically detect and parse this file

**Google Colab:**
- Add your API key as a Colab secret named `GOOGLE_API_KEY`
- The notebook will use the Colab userdata API

### Environment Variables (Optional)

You can also set the API key as an environment variable:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## 📖 Usage

### Running the Demo

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the demo notebook**
   - Navigate to `gemini_2_5_flash_demo.ipynb`
   - Run all cells to see the complete demonstration

### Notebook Sections

The notebook is organized into the following sections:

1. **Setup**: Install dependencies and configure API authentication
2. **Text Input**: Generate creative stories and analyze text content
3. **Image Input**: Process and describe images
4. **PDF Processing**: Extract and summarize document content
5. **Video Analysis**: Extract frames and analyze video content
6. **Audio Processing**: Transcribe and analyze audio files
7. **Summary**: Comprehensive overview of all inputs and responses

### Sample Files

The project includes sample files for testing:
- `phongnha.png` - Sample image for analysis
- `pytorch.png` - PyTorch course image
- `markov.pdf` - Sample PDF document
- `halong.mp4` - Sample video file
- `enigma.mp3` - Sample audio file

## 🔍 Key Features Demonstrated

### Text Processing
- Creative story generation
- Content analysis and summarization
- Natural language understanding

### Image Analysis
- Detailed image description
- Object recognition and scene analysis
- Visual content interpretation

### Document Processing
- PDF text extraction
- Document summarization
- Research paper analysis

### Video Processing
- Direct video file upload with `google.genai`
- Video content analysis and summarization
- Educational content generation (quizzes)

### Audio Processing
- Direct audio file processing with `types.Part.from_bytes()`
- Speech transcription and audio content analysis
- Multimodal audio understanding

## 🚨 Troubleshooting

### Common Issues

**1. API Key Not Found**
- Ensure your API key is correctly placed in `~/Documents/LangGraph-Credentials/.env.local`
- Check that the file contains `GOOGLE_API_KEY=your_api_key_here` format
- Verify there are no extra spaces or characters around the key

**2. FFmpeg Not Found**
- Install FFmpeg on your system:
  - **macOS**: `brew install ffmpeg`
  - **Ubuntu/Debian**: `sudo apt install ffmpeg`
  - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html)

**3. MoviePy Import Errors**
- Try reinstalling: `pip uninstall moviepy && pip install moviepy`
- Ensure you have the latest version: `pip install --upgrade moviepy`

**4. File Download Issues**
- Check your internet connection
- Verify that the sample file URLs are accessible
- Try running the notebook in Google Colab for better file handling

### Performance Tips

- Use smaller files for faster processing
- Consider using GPU acceleration for video processing
- Monitor API usage to avoid rate limits

## 📊 Project Structure

```
Gemini/
├── gemini_2_5_flash_demo.ipynb    # Main demonstration notebook
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore patterns
├── README.md                      # This file
├── enigma.mp3                     # Sample audio file
├── halong.mp4                     # Sample video file
├── markov.pdf                     # Sample PDF document
├── phongnha.png                   # Sample image
├── pytorch.png                    # Sample image
└── gemini-2.5-flash-demo/         # Additional demo files
    └── sample-files/              # Sample files directory
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for providing the Gemini API
- The open-source community for the various libraries used
- Contributors who helped improve this demonstration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the notebook comments and documentation
3. Open an issue on GitHub
4. Contact the maintainers

## 🔗 Useful Links

- [Google GenAI Documentation](https://googleapis.github.io/python-genai/)
- [Google Generative AI Documentation](https://ai.google.dev/docs)
- [Gemini API Reference](https://ai.google.dev/api/rest)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

---

**Happy coding! 🚀**
