def detect_palindrome(word):
    reversedstring = ''.join(word[::-1].lower().split())
    print(reversedstring)
    if reversedstring == ''.join(word.lower().split()):
        return True
    else:
        return False