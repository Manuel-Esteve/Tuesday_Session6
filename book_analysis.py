from enum import unique

import requests

from find_words_in_file import punctuation_remove, punctuation_space

book = requests.get('https://www.gutenberg.org/cache/epub/345/pg345.txt')
lines = book.text.split('\n')

punctuation_remove = ",.?!;"
punctuation_space = "'\"([=-_"
words = {}
for line in lines:
    for c in punctuation_remove:
        line = line.replace(c, "")
        words = line.split()
    for c in punctuation_space:
        line = line.replace(c, "")
        words = line.split()
    for words in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0) + 1

print(unique_words)
print(unique_words['the'])
print(unique_words['mina'])
print(unique_words['johnathan'])