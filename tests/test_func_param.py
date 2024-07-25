"""
* 17192 The Raven
* 932 Fall of the House of Usher
* 1063 Cask of Amontillado
* 10031 The Poems
* 14082 And Le Corbeau

Write a test for ALL the English files together. 
"""


from typing import Literal
import pytest
from collections import Counter
import requests
import sys
import os
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fju4ek_DS5111su24_lab_01.src.raven import tokenize



def tokenize(raven):
	# GIVEN a string text
	book_ids = ("17192", "932", "1063", "10031")
	all_text = ""
	
	# Loop through `book_ids` and download each book
	for id in book_ids: 
		url = f"https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"
		response = requests.get(url)
		text = response.text
		all_text += text	
	words = all_text.split()
	count_words = Counter(words)
	print(f"Total Word Count: {len(words)}")
	
	# WHEN the count_words function is called
	words = raven.split()
	
	# THEN it should return a dictionary with the words as keys, and their counts as value
	assert count_words == Counter(words), f"Tokenizer failed on sample text: {words}"

@pytest.mark.parametrize(
	"count_words",
	[
		("The Raven"),
		("Fall of the House of Usher"),
		("Cask of Amontillado"),
		("The Poems"),
		("And Le Corbeau")
	],
)

def test_tokenize(count_words: Literal['The Raven'] | Literal['Fall of the House of Usher'] | Literal['Cask of Amontillado'] | Literal['The Poems']):
	tokenize(count_words)

if __name__ == "__main__":
	pytest.main()

