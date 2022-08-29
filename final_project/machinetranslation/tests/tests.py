import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_input_not_null(self):
        self.assertEqual(english_to_french(None),'Cannot be null')
    
    def testHello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test_input_not_null(self):
        self.assertEqual(french_to_english(None),'Cannot be null')
    
    def testHello(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    

unittest.main()