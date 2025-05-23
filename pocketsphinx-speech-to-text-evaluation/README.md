# Speech Recognition Project


This project utilizes the pocketsphinx library to recognize text from audio files. It is structured to facilitate easy development, testing, and usage of speech recognition capabilities.

## What is pocketsphinx

`pocketsphinx` is an open-source speech-to-text (STT) engine developed by Carnegie Mellon University as part of the CMU Sphinx project. It is designed for embedded and resource-constrained environments, offering offline speech recognition capabilities without requiring an internet connection. While it was a significant advancement in its time, the quality of speech recognition provided by `pocketsphinx` is now considered quite limited by modern standards.

### STT Quality Comparison

- **pocketsphinx**: Recognition accuracy is generally low, especially for natural, conversational, or noisy audio. It often struggles with real-world audio and produces many errors, as demonstrated in this project.
- **Modern STT Technologies**: Recent advances in speech recognition leverage large language models (LLMs) and deep learning, such as OpenAI Whisper and Microsoft Phi. These models provide much higher accuracy, robustness to accents and noise, and support for multiple languages. They are suitable for both real-time and batch processing, and are widely adopted in industry applications.

**Summary:** While `pocketsphinx` is useful for simple, offline, or embedded use cases, it is not recommended for applications requiring high-quality or reliable speech-to-text results. Modern LLM-based STT solutions are far superior in terms of accuracy, speed, and versatility.

## Project Structure

The project is organized as follows:

```text
speech-recognition-project/
├── .venv/                   # Virtual environment for package management
├── src/                     # Source code for the application
│   ├── __init__.py          # Marks the src directory as a package
│   ├── pocketsphinx_app.py  # Main application logic for speech recognition
│   └── utils/               # Utility functions for audio processing
│       ├── __init__.py      # Marks the utils directory as a package
│       └── audio_processing.py # Functions for loading and validating audio files
├── tests/                   # Unit tests for the application
│   ├── __init__.py          # Marks the tests directory as a package
│   └── test_recognition.py  # Tests for the speech recognition functionality
├── data/                    # Directory for sample audio files
│   └── samples/             # Sample .wav files for testing
├── model/                   # Directory for speech recognition models
│   └── en-us/               # English model files (dictionary, language model, etc.)
├── requirements.txt         # Required packages for the project
├── setup.py                 # Configuration file for packaging the project
├── run-time.sh              # Script for measuring recognition runtime
├── test-results.md          # Test and runtime results
├── LICENSE.md               # License information
├── output_audio.txt         # Example output file for recognized text
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd speech-recognition-project
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Model Installation

The speech recognition model files are required for the application to work. Download the English model from the official CMU Sphinx website:

1. Download the model archive (e.g., `en-us-5.2.tar.gz`) from:
   https://github.com/cmusphinx/pocketsphinx/tree/master/model

2. Extract the contents and place the `en-us` folder inside the `model` directory at the project root, so the structure is:
   ```
   model/
     en-us/
       cmudict-en-us.dict
       en-us.lm.bin
       ...
   ```

Alternatively, you can use the provided `model/en-us` if it already exists in the repository.

## Usage

To recognize speech from an input audio file, run the following command from the project root:

```bash
python src/pocketsphinx_app.py -i data/samples/valid_audio.wav -o output_audio.txt
```

Replace `data/samples/valid_audio.wav` with the path to your audio file and `output_audio.txt` with the desired output file for the recognized text.

## Testing

To run the unit tests, ensure the virtual environment is activated and execute:

```bash
pytest tests/
```

## Evaluation

### Runtime Performance

The current implementation using `pocketsphinx` exhibits slow processing times for audio files. For example, recognizing a 3-second audio file (`valid_audio-03s.wav`) takes approximately 18 seconds, while a 30-second audio file (`valid_audio-30s.wav`) takes nearly 3 minutes. This performance may not be suitable for real-time or large-scale applications and suggests a need for optimization or consideration of alternative speech recognition engines for faster results.

### Test Results

All unit tests failed during evaluation:

- The test for valid audio did not produce the expected transcription. Instead of the correct phrase ("This is Guardian"), the output was inaccurate (e.g., "a hat hacker an an i in the eu").

- The test for invalid audio did not raise an exception as expected, indicating insufficient error handling for non-speech or corrupted audio files.

These results highlight the need for improvements in both recognition accuracy and error handling within the application.

## Conclusion

Testing `pocketsphinx` was an interesting and fun experience. However, the recognition quality is very low and not suitable for practical use — it's not recommended to rely on it for speech-to-text tasks. For much better results, consider using modern speech-to-text large language models (LLMs) such as OpenAI Whisper or Microsoft Phi.
