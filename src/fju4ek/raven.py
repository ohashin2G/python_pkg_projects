"""
* 17192 The Raven
* 932 Fall of the House of Usher
* 1063 Cask of Amontillado
* 10031 The Poems
* 14082 And Le Corbeau

"""
import sys
from collections import Counter
import requests

def tokenize(somestr):
	# GIVEN a string text
	
    book_ids = ("17192", "932", "1063", "10031", "14082")
    all_text = ""
    # Loop through `book_ids` and download each book
    for id in book_ids: 
       url = f"https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"
    response = requests.get(url)
    text = response.text
    words = text.split()
    count_words = Counter(words)
    print(f"Book ID: {id}, Word Count: {len(words)}")

 	# WHEN the count_words function is called
    words = all_text.split()

### TESTS 
    # THEN it should return a dictionary with the words as keys, and their counts as value
    assert count_words,  f"Tokenizer failed on sample text: {words}"

### CLI EXECUTION
if __name__ == "__main__":
    import sys
    #tokenize("sample_text")
    print(tokenize("sample_text"))

