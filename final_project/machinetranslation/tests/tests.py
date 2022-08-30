import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_input_not_null(self):
        self.assertEqual(englishToFrench(None),'Cannot be null')
    
    def testHello(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test_input_not_null(self):
        self.assertEqual(frenchToEnglish(None),'Cannot be null')
    
    def testHello(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    

unittest.main()