#Given a number num = 456, write a Python program using a while loop to calculate the sum of its digits and print the result.
num = 456
sum_of_digits = 0

while num > 0:
    digit = num % 10         # Get the last digit
    sum_of_digits += digit   # Add it to the sum
    num //= 10              # Remove the last digit

print(sum_of_digits)        # Output: 15

    