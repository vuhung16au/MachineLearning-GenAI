#!/bin/zsh

# Script to run speech-to-text on two audio files and measure execution time

echo "Processing valid_audio-03s.wav..."
time python3 src/pocketsphinx_app.py -i data/samples/valid_audio-03s.wav -o data/samples/valid_audio-03s.txt

echo "Processing valid_audio-30s.wav..."
time python3 src/pocketsphinx_app.py -i data/samples/valid_audio-30s.wav -o data/samples/valid_audio-30s.txt
