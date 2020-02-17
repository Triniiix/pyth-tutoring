from flask import Flask
from .palindrome import detect_palindrome
app = Flask(__name__)

@app.route("/palindrome")
def palindrome():
	word = "Racecar"
	is_palindrome = detect_palindrome(word)
	is_palindrome = word + ' is a palindrome' if is_palindrome else word + ' is not a palindrome'
	return is_palindrome
