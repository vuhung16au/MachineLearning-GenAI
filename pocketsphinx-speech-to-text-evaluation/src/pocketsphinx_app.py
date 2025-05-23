def recognize_speech(input_audio, output_audio):
    from pocketsphinx import AudioFile
    import os

    # Use local model directory
    model_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'en-us')
    dict_path = os.path.join(model_dir, 'cmudict-en-us.dict')
    lm_path = os.path.join(model_dir, 'en-us.lm.bin')

    config = {
        'verbose': False,
        'audio_file': input_audio,
        'hmm': model_dir,
        'dict': dict_path,
        'lm': lm_path
    }

    audio = AudioFile(**config)
    recognized_text = ""

    for phrase in audio:
        recognized_text += str(phrase) + "\n"

    with open(output_audio, 'w') as f:
        f.write(recognized_text)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Recognize speech from an audio file.')
    parser.add_argument('-i', '--input', required=True, help='Input audio file (.wav)')
    parser.add_argument('-o', '--output', required=True, help='Output text file to save recognized speech')

    args = parser.parse_args()
    recognize_speech(args.input, args.output)