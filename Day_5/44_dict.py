#Write Python code to access the value for key "Alice" using the get() method from a dictionary named grades containing "Alice": 85, "Bob": 90 and print it.
def main():
   grades = {"Alice": 85, "Bob": 90}
   Alice = grades.get("Alice")
   print(Alice)
if __name__ == "__main__":
    main()
    
