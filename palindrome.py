"""
A palindrome is a word that is spelled the same way
forwards and backwards.
Examples: racecar, mom, dad
"""

def detect_palindrome(word):
	word_reversed = ''.join(word[::-1].lower().split())
	return word == word_reversed
