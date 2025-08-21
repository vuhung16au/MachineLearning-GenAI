# MLX-LM Project

A Python project demonstrating the use of MLX-LM (Machine Learning eXchange Language Models) for text generation and chat applications on Apple Silicon.

## What is MLX-LM?

MLX-LM is a Python package for generating text and fine-tuning large language models on Apple silicon with MLX. It provides seamless integration with the Hugging Face Hub, allowing you to easily use thousands of LLMs with a single command.

### Key Features

- **Hugging Face Hub Integration**: Access thousands of LLMs with a single command
- **Model Quantization**: Support for quantizing and uploading models to the Hugging Face Hub
- **Fine-tuning Capabilities**: Low-rank and full model fine-tuning with support for quantized models
- **Distributed Computing**: Distributed inference and fine-tuning with `mx.distributed`
- **Streaming Generation**: Real-time text generation with streaming capabilities
- **Prompt Caching**: Efficient handling of long prompts and generations
- **Command Line Interface**: Easy-to-use CLI for model operations

## What Models are Available?

MLX-LM supports thousands of Hugging Face format LLMs. The MLX Community on Hugging Face provides a vast collection of optimized models, including:

### Popular Model Families
- **Mistral Models**: Mistral-7B, Mixtral-8x7B, and variants
- **Llama Models**: Llama 2, Llama 3, Llama 3.1, Llama 3.2 (including vision models)
- **Phi Models**: Microsoft's Phi-2, Phi-3, and variants
- **Qwen Models**: Qwen 1.5, Qwen 2.5 series (0.5B to 72B parameters)
- **Gemma Models**: Google's Gemma 2B, 7B, 9B, and 27B variants
- **Code Models**: CodeGemma, DeepSeek Coder, and specialized coding models
- **Vision Models**: Llama 3.2 Vision, Command Vision, and multimodal models

### Model Variants Available
- **Quantized Models**: 4-bit, 8-bit quantized versions for efficiency
- **Instruction-tuned**: Models optimized for chat and instruction following
- **Base Models**: Foundation models for fine-tuning
- **Specialized Models**: Code generation, reasoning, and domain-specific models

### Examples of Supported Models
- `mlx-community/Qwen2.5-0.5B-Instruct-4bit` (used in this project)
- `mlx-community/Meta-Llama-3-8B-Instruct-4bit`
- `mlx-community/Phi-3-mini-4k-instruct-4bit`
- `mlx-community/DeepSeek-V3-0324-4bit`
- `mlx-community/whisper-large-v3-mlx` (speech recognition)

## Why Run MLX-LM on macOS Silicon?

### Performance Benefits
- **Native Apple Silicon Optimization**: MLX is specifically designed for Apple's M-series chips
- **Unified Memory Architecture**: Leverages the unified memory system for efficient model loading
- **Metal Performance Shaders**: GPU acceleration through Metal framework
- **Memory Efficiency**: Optimized memory management for large language models

### Technical Advantages
- **No External Dependencies**: Runs natively without CUDA or other external libraries
- **Fast Model Loading**: Efficient model loading and caching mechanisms
- **Low Latency**: Optimized for real-time inference and chat applications
- **Energy Efficiency**: Better power management compared to traditional GPU solutions

### Developer Experience
- **Simple Installation**: Easy setup with pip or conda
- **Python Native**: Full Python API with familiar syntax
- **Hugging Face Integration**: Seamless access to the largest model repository
- **Active Community**: Strong support from the MLX community

## Prerequisites

- Python 3.8 or higher
- macOS with Apple Silicon (M1/M2/M3/M4 chips)
- 8GB+ RAM (16GB+ recommended for larger models)

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

## Advanced Usage

### Command Line Interface

You can also use MLX-LM directly from the command line:

```bash
# Generate text with a specific model
mlx_lm.generate --model mlx-community/Qwen2.5-0.5B-Instruct-4bit --prompt "Hello, world!"

# Start an interactive chat
mlx_lm.chat --model mlx-community/Qwen2.5-0.5B-Instruct-4bit

# Convert and quantize models
mlx_lm.convert --hf-path mistralai/Mistral-7B-Instruct-v0.3 -q
```

### Python API

```python
from mlx_lm import load, generate

# Load a model
model, tokenizer = load("mlx-community/Qwen2.5-0.5B-Instruct-4bit")

# Generate text
prompt = "Write a story about Einstein"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)

text = generate(model, tokenizer, prompt=prompt, verbose=True)
print(text)
```

## Features

- **Fast Model Loading**: Uses quantized models for quick startup
- **Interactive Chat**: Real-time conversation with the AI assistant
- **Error Handling**: Graceful error handling for failed generations
- **Clean Output**: Automatic cleanup of response formatting
- **Model Quantization**: Support for 4-bit and 8-bit quantized models
- **Streaming Generation**: Real-time text generation capabilities

## Model Information

This project uses the `mlx-community/Qwen2.5-0.5B-Instruct-4bit` model, which is:
- A 0.5 billion parameter model
- Quantized to 4-bit precision for efficiency
- Optimized for instruction following
- Fast enough for real-time chat applications
- Small enough to run on devices with limited memory

## Troubleshooting

- **Model Download**: The first run will download the model files (~100MB)
- **Memory Usage**: Ensure you have sufficient RAM for model loading
- **Python Version**: Make sure you're using Python 3.8 or higher
- **Virtual Environment**: Always activate the virtual environment before running scripts
- **Apple Silicon**: This project is optimized for Apple Silicon chips (M1/M2/M3/M4)

## Resources

- [MLX-LM PyPI Package](https://pypi.org/project/mlx-lm/)
- [MLX Community on Hugging Face](https://huggingface.co/mlx-community)
- [MLX Documentation](https://ml-explore.github.io/mlx/)
- [Qwen2.5 Model Information](https://huggingface.co/mlx-community/Qwen2.5-0.5B-Instruct-4bit)
- [MLX My Repo](https://huggingface.co/spaces/mlx-community/mlx-my-repo) - Convert and upload models to MLX format