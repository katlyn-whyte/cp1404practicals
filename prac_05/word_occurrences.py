"""
Word Occurrences
estimate: 30 minutes
Actual: 40 minutes
"""
words_to_count ={}
text = input("Text: ")
words = text.split()
for word in words:
    number_of_words = words_to_count.get(word, 0)
    words_to_count[word] = number_of_words + 1
words = list(words_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {words_to_count[word]}")
