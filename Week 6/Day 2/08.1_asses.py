input_string = "Hello, World!"
vowels = 'aeiou'

# This single line performs the count
vowel_count = sum(1 for char in input_string if char.lower() in vowels)

print(f"Number of vowels: {vowel_count}")
# Output: Number of vowels: 3