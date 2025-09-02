#Exercise 4.1: Count Vowels 
# Task: Count how many vowels (a, e, i, o, u) are in a given sentence. Make it case-insensitive. 
# Given: sentence = "Python Programming is Amazing!" 
# Expected Output: 
# The sentence has 9 vowels 
# Vowels found: o, o, a, i, i, A, a, i, 
# Your solution here:
# Create a vowels string and check each character in sentence
sentence = "Python Programming is Amazing!"
vowels = "aeiouAEIOU"
found_vowels = []

for i in sentence:
    if i in vowels:
        found_vowels.append(i)
print(f"The sentence has {len(found_vowels)} vowels")
print("Vowels found:", ", ".join(found_vowels))





