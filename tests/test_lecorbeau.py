"""
17192 The Raven
932 Fall of the House of Usher
1063 Cask of Amontillado
10031 The Poems
14082 And Le Corbeau.

Finally, write a test for Le Corbeau for each of your functions using the following as the text
"""

import pytest
from string import punctuation
import re
from collections import Counter
import requests


corbeau = ("""_Mais le Corbeau, perché solitairement sur ce buste placide, parla
ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
que je fis à peine davantage que marmotter «D'autres amis déjà ont
pris leur vol--demain il me laissera comme mes Espérances déjà ont
pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_""")

def text():
	return corbeau


@pytest.fixture()
def clean_text():
    """Return cleaned text with no punctuation."""
    return corbeau.lower().translate(str.maketrans('', '', punctuation))


def test_clean_text(clean_text: str):
    """Use fixture return value in a test."""
    assert isinstance(clean_text, str), f"expected str but got {type(clean_text)}"


@pytest.fixture()
def tokenizer(clean_text):
    """Return a list of words."""
    try:
        return re.findall(r'\b\w+\b', clean_text)
    except TypeError:
        print("This test should fail")


@pytest.fixture()
def test_tokenizer(tokenizer: list[str]):
    """Use fixture return value in a test."""
    try:
        assert isinstance(tokenizer, list), f"expected list but got {type(tokenizer)}"
    except TypeError:
        print("This test should fail")

def test_error(test_tokenizer: None):
    """Use fixture return value in a test."""
    assert test_tokenizer is None, f"expected None but got {test_tokenizer}"



@pytest.fixture()
def count_words(tokenizer):
    """Return a dictionary of word counts."""
    try:
        return Counter(tokenizer)
    except TypeError as e:
        print("An error occurred while counting words:", e)
 

def test_count_words(tokenizer: dict[str, int], count_words: dict[str, int]):
    """Use fixture return value in a test."""
    assert not clean_text  == "" , "should not be empty"
    assert isinstance(count_words, dict), f"expected dict but got {type(count_words)}"
    assert count_words,  f"Tokenizer failed on sample text: {clean_text}"



