import re

text = "Python is easy. My age is 21. Contact me at 9876543210."

# 1. re.search() - Find the first match
result = re.search(r"\d+", text)
print("Search:", result.group())

# 2. re.match() - Check the beginning of the string
result = re.match(r"Python", text)
print("Match:", result.group() if result else "No match")

# 3. re.findall() - Find all numbers
result = re.findall(r"\d+", text)
print("Findall:", result)

# 4. re.sub() - Replace numbers with ***
result = re.sub(r"\d+", "***", text)
print("Sub:", result)

# 5. re.split() - Split the text at spaces
result = re.split(r"\s+", text)
print("Split:", result)

# 6. re.fullmatch() - Check whether the string contains only digits
number = "12345"
result = re.fullmatch(r"\d+", number)
print("Fullmatch:", "Only digits" if result else "Not only digits")