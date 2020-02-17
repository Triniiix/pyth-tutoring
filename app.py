from flask import Flask
from .palindrome import detect_palindrome
app = Flask(__name__)

@app.route("/palindrome")
def palindrome():
	word = "Racecar"
	is_palindrome = detect_palindrome(word)
	is_palindrome = 'is a palindrome' if is_palindrome else 'is not a palindrome'
	return detect_palindrome()
