def analyze_string(str):
    # Code Starts

    # Write your code here 
    return {

        "Length": len(str),
        "Upper": str.upper(),
        "Lower": str.lower()
    }

    # Code Ends

# Predefined inputs
text = "Hello World"

# Function call
print(analyze_string(text))