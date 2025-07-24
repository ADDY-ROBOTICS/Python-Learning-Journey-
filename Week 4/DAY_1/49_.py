def main():
    start , end = 1 , 100 
    count = 0
    for i in range(start,end+1):
        if i % 2 == 0:
            count += 1
    print("The total number of even numbers from", start, "to", end, "is", count)       
if __name__ == "__main__":
    main()
    
#Given two variables start and end, write a Python program to count how many even numbers are present in the range from start to end (inclusive). Use a for loop with the variable i to iterate through the range and a counter variable count to keep track of even numbers. Finally, print the value of count.
