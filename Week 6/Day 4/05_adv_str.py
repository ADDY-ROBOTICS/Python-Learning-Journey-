#Write a Python program to decode a UTF-8 encoded string back to its original text.
def main():
    text = "Hello World"
    #Encoding the text 
    utf8_bytes = text.encode("utf-8")
    #Decoding the text 
    decoded_bytes = utf8_bytes.decode("utf-8")
    #Getting the orignal text back 
    print(decoded_bytes)

if __name__ == "__main__":
    main()
    