# Importiamo il modulo unittest.
# unittest è la libreria standard di Python per creare ed eseguire unit test.
import unittest

# Importiamo la funzione emotion_detector dal package EmotionDetection.
# Questa è la funzione che vogliamo testare.
from EmotionDetection import emotion_detector


# Creiamo una classe di test.
# Per usare unittest, la classe deve ereditare da unittest.TestCase.
class TestEmotionDetection(unittest.TestCase):

    # Testiamo una frase che dovrebbe avere come emozione dominante "joy".
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    # Testiamo una frase che dovrebbe avere come emozione dominante "anger".
    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    # Testiamo una frase che dovrebbe avere come emozione dominante "disgust".
    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    # Testiamo una frase che dovrebbe avere come emozione dominante "sadness".
    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    # Testiamo una frase che dovrebbe avere come emozione dominante "fear".
    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


# Questa parte permette di eseguire i test direttamente con:
# python3 test_emotion_detection.py
if __name__ == "__main__":
    unittest.main()