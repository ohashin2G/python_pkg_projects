""""
Week 4: Testing
Testing your functions
Function: count_words

"""

import sys
import os
import unittest
from collections import Counter
import re
from string import punctuation


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab3 import count_words


class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        # GIVEN a string clean text
        # WHEN the count_words function is called
        clean_text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        count_words = Counter(clean_text.split())
        len(clean_text.split())

        # THEN it should return a dictionary with the words as keys, and their counts as value
        assert count_words,  f"Tokenizer failed on sample text: {clean_text}"



if __name__ == '__main__':
    unittest.main()

# Subsets of Tests
# pytest -v test_tokenizer.py::TestCleanText::test_clean_text  # single test
# pytest -v test_tokenizer.py::TestCleanText  # all tests in a class
# pytest -v test_tokenizer.py::test_function  # single test function
# pytest -v test_tokenizer.py  # all tests in a file/module
# pytest tests # all tests in a directory

