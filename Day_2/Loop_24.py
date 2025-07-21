 fn_1 = 0
 fn_2 = 1
while fn_2 < 100:
    print(fn_2)
    fn_1, fn_2 = fn_2, fn_1 + fn_2  # Update to the next Fibonacci number
    fn_2 += 1
    # Update to the next Fibonacci number
print("Fibonacci sequence up to 100:")
    print(fn_1, end=' ')