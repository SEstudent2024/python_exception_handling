# Exceptional Weather Forecast
# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a 
# weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

user_input = input("Enter a temperature in Fahrenheit: ")

# Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process. 
# What happens if they type out "thirty" instead of doing 30?

def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius"""
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
    except ValueError:
        print("Error: Please enter a valid number for the temperature in Fahrenheit")
    
# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius")

# Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

    finally:
        print("Thank you for using the weather forecast application.")

convert_fahrenheit_to_celsius(user_input)

