'''Write a Python program that calculates a student's final grade based
 on homework, quiz, and exam scores. The function should take three keyword arguments.'''
def calculate_grade(h, q, e):
    # Code Starts

    # Write your code here 
   # return (homework*0.3)+(quiz*0.2)+(exam*0.5)This uses variables from outside the function, not h, q, and e
   #While this works in this specific script, it's a major bug in real-world code because the function is not self-contained. It should always use the parameters it receives
    return (h * 0.3) + (q * 0.2) + (e * 0.5)  # This correctly uses the parameters passed into the function

    # Code Ends

# Predefined inputs
homework = 85
quiz = 90
exam = 78

# Function call
print(calculate_grade(homework, quiz, exam))