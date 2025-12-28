import re
def is_palindrome(string):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    return cleaned == cleaned[::-1]