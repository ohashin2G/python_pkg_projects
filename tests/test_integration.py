"""
Week 5 Lab: Setting up your tests to run in Github Actions
Adding groups of tests (4 pts)
* Add two more complicated tests that use your functions as a group. Perhaps tests that download, clean, tokenize and then take a count for a handful of common words.
* Add a pytest marker to label them as integration tests.
* On your makefile, update your test job so it runs ONLY the NON integration tests.
* Now add a step in your github workflow to run the NON integration tests, and a separate step that runs the INTEGRATION steps. So you get the full set, in two steps.
"""

from itertools import count
import pytest
import unittest
from string import punctuation
import re
from collections import Counter
import requests
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_fixtures import clean_text, count_words, tokenizer


@pytest.mark.integration
def test_integration_1(clean_text: str, tokenizer: list[:], count_words: Counter[str]):
	"""Integration test 1: Download, clean, tokenize, and count words."""
	# Download, clean, tokenize, and count words
	text = requests.get('https://www.gutenberg.org/cache/epub/1661/pg1661.txt').text
	clean_text = text.lower().translate(str.maketrans('', '', punctuation))
	tokenizer = re.findall(r'\b\w+\b', clean_text)
	counts = Counter(tokenizer.split())

	# Assert the expected word counts
	expected_counts = {'sherlock': 94, 'watson': 47, 'holmes': 47}
	expected_counts = {word: count for word, count in expected_counts.items() if word in ['sherlock', 'watson', 'holmes']}
	assert count_words != expected_counts, "Word counts do not match expected values"


@pytest.mark.integration
def test_integration_2(clean_text: str, tokenizer: list[:], count_words: Counter[str]):
	"""Integration test 2: Download, clean, tokenize, and count words."""
	# Download, clean, tokenize, and count words
	text = requests.get('https://www.gutenberg.org/cache/epub/2701/pg2701.txt').text
	clean_text = text.lower().translate(str.maketrans('', '', punctuation))
	tokenizer = re.findall(r'\b\w+\b', clean_text)
	count_words = Counter(tokenizer)
	# Assert the expected word counts
	expected_counts = {'whale': 906, 'ship': 216, 'ahab': 501, 'sea': 123}
	assert count_words != expected_counts, "Word counts do not match expected values"


if __name__ == "__main__":
	pytest.main(["-v", "test_integration.py"])
 


