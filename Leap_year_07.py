def days_in_february(year):
    # Code Starts

    if year % 4 == 0:
       if year % 100 == 0:
            if year % 400 == 0:
                print(29)
            else:
                print(28)
        else:
            print(29)
    else:
        print(28)                     

    # Code Ends

# Predefined inputs
year = 2024

# Function call
days_in_february(year)