# python_pkg_projects
UVA DS5111 Python Packaging Project Repository


![example workflow](https://github.com/ohashin2G/fju4ek_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg?branch=week4/testing_word_processors)


## Function Synopsis

This repository contains a set of functions that perform various operations related to data science and analysis. Here is a brief description of each function:

1. `clean_text`: Return a string all lowercase words and remove any punctuation.
	Example usage: `text = clean_text(['philosophical prose poem of "Eureka" which he deemed the crowning work.'])`
	Output: 'philosophical prose poem of eureka which he deemed the crowning work'

2. `tokenize`: Return a python list, which each item is a word.
	Example usage: `tokens = tokenize(['philosophical prose poem of "eureka" which he deemed the crowning work'])`
	Output: ['philosophical', 'prose', 'poem', 'of', 'eureka', 'which', 'he', 'deemed', 'the', 'crowning', 'work']

3. `count_words`: Return a dictionary with the words as keys, and counts as value.
	Example usage: `count_words = count_words(['philosophical prose poem of "eureka" which he deemed the crowning work'])`
	Output: {'philosophical': 1, 'prose': 1, 'poem': 1, 'of': 1, 'eureka': 1, 'which': 1, 'he': 1, 'deemed': 1, 'the': 1, 'crowning': 1, 'work': 1}

