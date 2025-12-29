def sort_words(string):
  a = string.split()
  a.sort(key = str.lower)
  return a


if __name__ == '__main__':
    print(sort_words('hello world'))  # false
    print(sort_words("Go hang a salami, I'm a lasagna hog."))  # true