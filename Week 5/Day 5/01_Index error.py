def main():
    my_list = [1, 2 , 3]

    try:
        third_item = my_list[3]
        print(f"The third item in my list is {third_item}")

    except IndexError:
        print("Could not receive the Third item because it doesn't exist ")
if __name__ == "__main__":
    main()
    
