from flask import Flask
app = Flask(__name__)
from .palindrome import detect_palindrome

@app.route("/", methods=['POST'])
def hello():
	word = 'mom'
	is_palindrome = detect_palindrome(word)
	# python ternary expression
	is_palindrome = 'is a palidrome' if is_palindrome else 'is not a palindrome'
	return f'{word} {is_palindrome}'

if __name__ == "__main__":
	app.run()