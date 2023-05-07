# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Ask the user for the operation to perform
while True:
    operation = input("Please choose a math operation (addition, subtraction, multiplication, division): ")
    # Ask the user for two numbers
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
    # Calculate the result based on the chosen operation
        while True:
            try:
                if operation == "addition":
                    result = num1 + num2
                elif operation == "subtraction":
                    result = num1 - num2
                elif operation == "multiplication":
                    result = num1 * num2
                elif operation == "division":
                    if num2 == 0:
                        raise ZeroDivisionError("Error: Cannot divide by zero.")
                    result = num1 / num2
                else:
                    raise ValueError("Error: Invalid operation")
                    break
            except ZeroDivisionError as e:
                print(f"Error: {str(e)} Please enter the second number again: ")
                num2 = float(input("Enter the second number: "))
            except ValueError as e:
                print(f"Error: {str(e)}")
                break
    # Print the result
    print("Result: ", result)
# Ask the user if they want to try again