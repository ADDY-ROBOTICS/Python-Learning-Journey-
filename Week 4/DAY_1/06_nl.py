#Write a program using nested loops to count total iterations when outer loop runs 5 times and inner loop runs 2 times
def main():
    count = 0
    for i in range(5):
        for j in range(2):
            count += 1
    print(count)        
            

if __name__ == "__main__":
    main()
    
