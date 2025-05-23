# `pocketsphinx` takes too long to recognize the text 

```bash
sh run-time.sh
Processing valid_audio-03s.wav...

real    0m18.066s
user    0m17.956s
sys     0m0.090s
Processing valid_audio-30s.wav...

real    2m51.670s
user    2m49.389s
sys     0m1.141s
```

# `pocketsphinx` failed to recognize the speech in the audio file. 

```python
pytest tests
=================================================== test session starts ====================================================
platform darwin -- Python 3.13.3, pytest-8.3.5, pluggy-1.6.0
rootdir: /Users/vuhung/Desktop/pocketsphinx/speech-recognition-project
collected 2 items                                                                                                          

tests/test_recognition.py F
F                                                                                         [100%]

========================================================= FAILURES =========================================================
________________________________ TestSpeechRecognition.test_recognize_speech_invalid_audio _________________________________

self = <tests.test_recognition.TestSpeechRecognition testMethod=test_recognize_speech_invalid_audio>

    def test_recognize_speech_invalid_audio(self):
        input_audio = 'data/samples/invalid_audio.wav'
        output_audio = 'output_audio.txt'
    
>       with self.assertRaises(Exception):
E       AssertionError: Exception not raised

tests/test_recognition.py:22: AssertionError
_________________________________ TestSpeechRecognition.test_recognize_speech_valid_audio __________________________________

self = <tests.test_recognition.TestSpeechRecognition testMethod=test_recognize_speech_valid_audio>

    def test_recognize_speech_valid_audio(self):
        input_audio = 'data/samples/valid_audio-03s.wav'
        expected_output = 'This is Guardian'
        output_audio = 'output_audio.txt'
    
        recognize_speech(input_audio, output_audio)
    
        with open(output_audio, 'r') as f:
            result = f.read().strip()
    
>       self.assertEqual(result, expected_output)
E       AssertionError: 'a hat hacker an an i in the eu' != 'This is Guardian'
E       - a hat hacker an an i in the eu
E       + This is Guardian

tests/test_recognition.py:16: AssertionError
================================================= short test summary info ==================================================
FAILED tests/test_recognition.py::TestSpeechRecognition::test_recognize_speech_invalid_audio - AssertionError: Exception not raised
FAILED tests/test_recognition.py::TestSpeechRecognition::test_recognize_speech_valid_audio - AssertionError: 'a hat hacker an an i in the eu' != 'This is Guardian'
==================================================== 2 failed in 18.65s ====================================================
```