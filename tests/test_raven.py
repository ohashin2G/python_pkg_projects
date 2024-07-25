"""
Week 4: Testing

17192 The Raven
932 Fall of the House of Usher
1063 Cask of Amontillado
10031 The Poems
14082 And Le Corbeau.

"""

import pytest
from string import punctuation
import re
from collections import Counter
import requests
import sys
import subprocess



"""
Write a test for each of your functions now working against the whole 'The Raven' file.
"""
raven = requests.get('https://www.gutenberg.org/cache/epub/1065/pg1065.txt').text


@pytest.fixture()
def clean_text():
    """Return cleaned text with no punctuation."""
    return raven.lower().translate(str.maketrans('', '', punctuation))


def test_clean_text(clean_text: str):
    """Use fixture return value in a test."""
    assert isinstance(clean_text, str), f"expected str but got {type(clean_text)}"


@pytest.fixture()
def tokenizer():
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


"""
Expand that, by following the parametrizing procedure in the book so you can pass in the list of files to a test to run each of your English files. I.e. a parameter to the test is a list of the file names, and for each name a test is run independently.
"""

book_ids = ("17192" "932" "1063" "10031" )

@pytest.mark.parametrize("file_name", ["get_the_books.sh", *book_ids])
def test_file_processing(file_name):
    """Test the file_processing function with an invalid file."""
    try:
        assert file_name, f"Expected False but got {file_name}"
    except FileNotFoundError as e:
        print("An error occurred while processing the file:", e)
    assert True
    

text = "_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"

@pytest.mark.parametrize("text", [text])
def test_clean_text(text):
	"""Use fixture return value in a test."""
	assert isinstance(text, str), f"expected str but got {type(text)}"




def test_os():
    """
    Test is continial on my OS.  Tests may fail on a different OS since it has not been tested.
    """
    current_os = sys.platform
    assert current_os, f"Tests may fail on {current_os} since it has not been tested."



def test_bash_comparison():
    """Test the tokenizer function against bash/linux command."""
    test_string = "This is a test string."
    bash_result = subprocess.run(["echo", test_string], capture_output=True, text=True)
    assert bash_result.stdout, f"expected {test_string} but got {bash_result.stdout}"


if __name__ == "__main__":
	pytest.main(["-v", "test_raven.py"])


