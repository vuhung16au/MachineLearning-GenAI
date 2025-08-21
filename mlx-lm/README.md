# MLX-LM Project

A Python project demonstrating the use of MLX-LM (Machine Learning eXchange Language Models) for text generation and chat applications.

## Prerequisites

- Python 3.13 or higher
- macOS (MLX is optimized for Apple Silicon)

## Setup Instructions

### 1. Create a Python Virtual Environment

First, navigate to the project directory and create a virtual environment:

```bash
cd /path/to/mlx-lm
python3.13 -m venv .venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment:

```bash
source .venv/bin/activate
```

You should see `(.venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 3. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install `mlx-lm>=0.12.0` and its dependencies.

## Usage

### Running hello.py

The `hello.py` script demonstrates a simple "Hello World" example with MLX-LM:

```bash
python hello.py
```

This script:
- Loads the `mlx-community/Qwen2.5-0.5B-Instruct-4bit` model
- Generates a response to the prompt "why sky is blue?"
- Displays the prompt and generated response

Example output:
```
Loading model...
Fetching 9 files: 100%|█████████████████████████████████████| 9/9 [00:00<00:00, 13847.67it/s]
Model loaded successfully!
Generating 'Hello World' response...

Prompt: why sky is blue?
Response: I have a question about the sky. I have seen many times that the sky is blue...

🎉 Hello World with MLX-LM complete!
```

### Running chat.py

The `chat.py` script provides an interactive chat interface:

```bash
python chat.py
```

This script:
- Loads the same model as hello.py
- Provides an interactive chat interface
- Allows you to have conversations with the AI assistant
- Type `/exit` or `/quit` to end the conversation

Example usage:
```
🤖 MLX-LM Chat Assistant
========================================
Loading model...
Fetching 9 files: 100%|█████████████████████████████████████| 9/9 [00:00<00:00, 28575.88it/s]
✅ Model loaded successfully!
You can start chatting now. Type '/exit' or '/quit' to end the conversation.
========================================

💬 You: hi
🤖 Assistant: Hello! How can I help you today?

💬 You: /exit
👋 Goodbye! Thanks for chatting!
```

## Features

- **Fast Model Loading**: Uses quantized models for quick startup
- **Interactive Chat**: Real-time conversation with the AI assistant
- **Error Handling**: Graceful error handling for failed generations
- **Clean Output**: Automatic cleanup of response formatting

## Model Information

This project uses the `mlx-community/Qwen2.5-0.5B-Instruct-4bit` model, which is:
- A 0.5 billion parameter model
- Quantized to 4-bit precision for efficiency
- Optimized for instruction following
- Fast enough for real-time chat applications

## Troubleshooting

- **Model Download**: The first run will download the model files (~100MB)
- **Memory Usage**: Ensure you have sufficient RAM for model loading
- **Python Version**: Make sure you're using Python 3.13 or higher
- **Virtual Environment**: Always activate the virtual environment before running scripts

## Resources

- [MLX-LM PyPI Package](https://pypi.org/project/mlx-lm/)
- [MLX Documentation](https://ml-explore.github.io/mlx/)
- [Qwen2.5 Model Information](https://huggingface.co/mlx-community/Qwen2.5-0.5B-Instruct-4bit)