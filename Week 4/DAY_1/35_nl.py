#Write a Python program to print the first 10 Fibonacci numbers (starting from 0, 1).
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# Print the first 10 Fibonacci numbers
print(fibonacci(10))
