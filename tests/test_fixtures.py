"""
Week 4: Testing
Testing your functions
Function: fixtures

Use a decorator and write a test for each of your functions against that one text string that is intended to fail on purpose.
Use the `skip` decorator for a test that hypothetically is expected to pass but can't be run.
"""

import pytest
from string import punctuation
import re
from collections import Counter



def text():
    return 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'


@pytest.fixture()
def clean_text():
    """Return cleaned text with no punctuation."""
    return text().lower().translate(str.maketrans('', '', punctuation))


def test_clean_text(clean_text: str):
    """Use fixture return value in a test."""
    assert isinstance(clean_text, str), f"expected str but got {type(clean_text)}"



@pytest.fixture()
def tokenizer(clean_text):
	"""Return a list of words."""
	try:
		return re.findall(r'\b\w+\b', clean_text)
	except TypeError:
		pytest.skip("This test should fail")

@pytest.fixture()
def test_tokenizer(tokenizer: list[str]):
	"""Use fixture return value in a test."""
	try:
		isinstance(tokenizer, list), f"expected list but got {type(tokenizer)}"
	except TypeError:
		pytest.skip("This test should fail")

def test_error(test_tokenizer: None):
	"""Use fixture return value in a test."""
	assert test_tokenizer is None, f"expected None but got {test_tokenizer}"



@pytest.fixture()
def count_words(tokenizer):
	"""Return a dictionary of word counts."""
	try:
		return dict(Counter(tokenizer))
	except TypeError as e:
		print("An error occurred while counting words:", e)
		return {}

def test_count_words(count_words: dict[str, int]):
	"""Use fixture return value in a test."""
	assert isinstance(count_words, dict), f"expected dict but got {type(count_words)}"

