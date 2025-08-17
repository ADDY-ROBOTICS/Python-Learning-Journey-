#Write a Python program that encodes the string 'Hello World 123!' using UTF-8 and prints the result. Then decode the encoded value back to a string and print it again.
def main():
    text = "Hello World 123!"
    utf_encoded = text.encode("utf-8")
    print(utf_encoded)

    utf_decoded = utf_encoded.decode("utf-8")
    print(utf_decoded)
    

if __name__ == "__main__":
    main()