#Exercise 4.2: Reverse Each Word 
# Task: Reverse each word in a sentence while keeping the word order the same. 
# Given: sentence = "Hello World Python" 
# Expected Output: 
# Original: Hello World Python 
# Reversed: olleH dlroW nohtyP,
# sentence = "Hello World Python" 
# # Your solution here: 
# # Hint: Use split() to get words, then reverse each word with [::-1]
sentence = "Hello World Python"

words = sentence.split()
reversed_words = [word[::-1] for word in words]
reversed_sentence = " ".join(reversed_words)

print("Original:", sentence)
print("Reversed:", reversed_sentence)
