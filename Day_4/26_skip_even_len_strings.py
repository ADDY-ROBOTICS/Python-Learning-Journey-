def main():
    words = ["cat", "dog", "bird", "snake"]
    for letter in words:
        if len(letter) % 2 == 0:
            continue
        print(letter)    
    

if __name__ == "__main__":
    main()
    
