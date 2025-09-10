#  .upper()
# Converts all characters in a string to uppercase.
text = "aliza"
print(text.upper())  # Output: ALIZA
#  .lower()
# Converts all characters in a string to lowercase. 
text = "HELLO"
print(text.lower())  # Output: hello
# 3. .strip()
# Removes leading and trailing spaces (spaces from beginning and end)
text = "   Hello Aliza   "
print(text.strip())  # Output: Hello Aliza

#Exersice 1

text = "    i want to become a PYTHON DEVELOPER    "

# 1. Remove extra spaces from both ends.
text = text.strip()
# 2. Convert the whole string to lowercase.
text = text.lower()
# 3. Convert the cleaned-up string to title case.
text = text.title()

#Exersice 2
text = "Welcome to Python Programming"

# 1. Check if the string starts with "Welcome"
text = "Welcome to Python Programming"
print(text.startswith("Welcome"))  
# 2. Check if the string ends with "Programming"
print(text.endswith("Programming"))
# 3. Check if it ends with "Python"
print(text.endswith("Python"))
