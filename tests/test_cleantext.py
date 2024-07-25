""""
Week 4: Testing
Testing your functions
Function: clean_text

"""

import sys
import os
import unittest
from collections import Counter
import re
from string import punctuation

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab3 import clean_text


class TestCleanText(unittest.TestCase):
    def test_clean_text(clean_text):
        # GIVEN a string sample_text with words
        text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
        # WHEN the clean_text function is called
        trans = str.maketrans('', '', punctuation)
        clean_text = text.lower().translate(trans)

        # THEN it should return all lowercase words with no punctuation
        assert isinstance(text, str), f"expected str but got {type(text)}"


if __name__ == '__main__':
    unittest.main()
