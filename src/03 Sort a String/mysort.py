def sort_words(string):
  a = string.split()
  a.sort(key = str.lower)
  return a