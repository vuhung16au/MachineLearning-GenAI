def load_wav_file(file_path):
    import wave
    import os

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    if not file_path.endswith('.wav'):
        raise ValueError("The file must be a .wav file.")

    with wave.open(file_path, 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)

    return params, frames

def validate_audio_file(file_path):
    import os

    if not os.path.isfile(file_path):
        return False, "File does not exist."
    
    if not file_path.endswith('.wav'):
        return False, "File is not a .wav file."
    
    return True, "File is valid."