#Write a Python program called show_info that takes name (required) and message (optional with default 'Hello'). Ensure name comes before message.
def show_info(name , message = "Hello"):
    print(f"{message}, {name}")
    
show_info("ADDY")
    