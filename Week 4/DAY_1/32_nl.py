#Write a Python program to print even numbers from 2 to 20 using a while loop.
def main():
    for i  in range(2,21):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    main()
    
    #using while loop
def main():
    num = 2 
    while num <= 20:
        print(num)
        num += 2

if __name__ == "__main__":
    main()
    