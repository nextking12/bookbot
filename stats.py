def word_count(text):
    words = text.split()
    return len(words)


char_values = {}
def char_count(text):
    words = text.split()
    chars = words.list().lower()

   # for char in chars:
