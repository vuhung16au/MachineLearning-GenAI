import unittest
from src.pocketsphinx_app import recognize_speech

class TestSpeechRecognition(unittest.TestCase):
    
    def test_recognize_speech_valid_audio(self):
        input_audio = 'data/samples/valid_audio-03s.wav'
        expected_output = 'This is Guardian'
        output_audio = 'output_audio.txt'
        
        recognize_speech(input_audio, output_audio)
        
        with open(output_audio, 'r') as f:
            result = f.read().strip()
        
        self.assertEqual(result, expected_output)

    def test_recognize_speech_invalid_audio(self):
        input_audio = 'data/samples/invalid_audio.wav'
        output_audio = 'output_audio.txt'
        
        with self.assertRaises(Exception):
            recognize_speech(input_audio, output_audio)

if __name__ == '__main__':
    unittest.main()