import re
def is_palindrome(string):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    return cleaned == cleaned[::-1]


if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true