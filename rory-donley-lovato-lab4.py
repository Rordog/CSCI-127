# -----------------------------------------+
# Rory Donley-Lovato                       |
# CSCI 127, Lab 4                          |
# Last Updated: 9/15/2020                  |
# -----------------------------------------|
# Word Counter                             |
# -----------------------------------------+

from collections import Counter

def make_word_list(sentence):
   punctuation = ".,!?;-'"
   word = ""
   for char in sentence:
      if char not in punctuation:
         word += char
   w = word.split(" ")
   return w

def count_freq_iteratively(words):
   sub = []
   for i in words:
      if i not in sub:
         sub.append(i)
   for i in sub:
      print(i, words.count(i))

def count_freq_recursively(words):
   print(Counter(words))
   
def main():
    user_input = input("Enter words: ")
    user_words = user_input.lower()
    words = make_word_list(user_words)
    print(words)
    print("Iterative Count: ")
    count_freq_iteratively(words)

    words.sort()
    print(words)
    print("Recursive Count: ")
    count_freq_recursively(words)

main()
