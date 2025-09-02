#Exercise 4.3: Simple Password Checker 
# Task: Check if a password meets these criteria: 
# At least 8 characters long 
# Contains at least one digit 
# Contains at least one uppercase letter
# Test with: 
# passwords = ["hello", "Hello123", "PASSWORD", "MyPass1"] 
# Expected Output: 
# hello: ❌ Too short, No digits, No uppercase 
# Hello123: ✅ Valid password 
# PASSWORD: ❌ No digits 
# MyPass1: ✅ Valid password,
# passwords = ["hello", "Hello123", "PASSWORD", "MyPass1"] 
# # Your solution here: # Check len(), .isdigit(), .isupper() methods 
# # Use any() function to check if any character meets criteria,
passwords = ["hello", "Hello123", "PASSWORD", "MyPass1"]

MIN_LEN = 7 

for pwd in passwords:
    reasons = []

    
    if len(pwd) < MIN_LEN:
        reasons.append("Too short")
    if not any(ch.isdigit() for ch in pwd):
        reasons.append("No digits")
    if not any(ch.isupper() for ch in pwd):
        reasons.append("No uppercase")

    if reasons:
        print(f"{pwd}: ❌ " + ", ".join(reasons))
    else:
        print(f"{pwd}: ✅ Valid password")


