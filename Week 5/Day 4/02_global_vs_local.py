count = 9
def increment_count():
    global count
    count += 1

increment_count()
print(f"The incremented count is: {count}")
