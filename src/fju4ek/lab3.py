"""
Week 3 Lab: python counter, cleaner, tokenizer

Functions:
- clean_text: should take a string, and should return all lowercase words,
and throw out any punctuation
- tokenize: should take a string and return a python list, where each item is
a word in the file
- count_words: should take a string and return a dictionary with the words 
as keys, and their counts as value
"""

from collections import Counter
import re
from string import punctuation

sample_text = 'philosophical prose poem of "Eureka," which he deemed the crowning work'

def clean_text(sample_text):
    """
    clean_text, should take a string, and should return all lowercase words, 
 	and throw out any punctuation

	Args:
		text (str): the sample text to be cleaned

	Returns:
		words: all lowercase words with no puctuation
	"""
    assert isinstance(
        sample_text, str), f"expected str but got {type(sample_text)}"

    trans = str.maketrans('', '', punctuation)
    assert not isinstance(trans, int)

    clean_text = sample_text.lower().translate(trans)
    assert isinstance(clean_text, str)
    assert not clean_text == "" , "should not be empty"

    return clean_text
    print(clean_text)
    
clean_text(sample_text)


def tokenize(clean_text):
    """
	tokenize should take a string and return a python list, where each item is a word in the file.
	Args:
		text (str): the clean text to be tokenized
	Returns:
		list: a python list, where each item is a word in the file
 	"""
    tokens = re.findall(r'\b\w+\b', clean_text)
    assert isinstance(tokenize(clean_text), list), f'Tokenizer failed on sample text: {clean_text}'
    return tokens
    print(tokens)




def count_words(clean_text):
    """
	Count_words should take a string and return a dictionary with the words as keys,
 	and their counts as value

	Args:
		text(str): the sample text to be counted
	Returns:
		dict: a dictionary with the words as keys, and their counts as value
	"""

    assert isinstance(
        clean_text, int), f"expected int but got {type(clean_text)}"

    txt = clean_text
    assert not txt == "" , "should not be empty"

    count_words = Counter(txt.split())
    assert isinstance(count_words, dict)

    count_words.most_common(2)
    assert isinstance(count_words.most_common(2), list)

    sum(count_words.values())
    assert isinstance(sum(count_words.values()), int)

    return len(clean_text.split())

if __name__ == "__main__":
    print(clean_text(sample_text))
