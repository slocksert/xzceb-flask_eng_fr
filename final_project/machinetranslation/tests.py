import unittest

from translator import french_to_english, english_to_french

class Test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test3(self):
        self.assertEqual(french_to_english(' '), ' ')

class Test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test3(self):
        self.assertEqual(english_to_french(' '), ' ')

unittest.main()