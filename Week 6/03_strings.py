import re 
pattern = r"\d+"
text = "I have 2 jerseys and 1 pair of studs"
numbers = re.findall(pattern, text)
print(numbers)