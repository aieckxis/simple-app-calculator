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
            print("\033[31mError: Invalid input. Please enter a number.\033[0m")
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
                    raise ZeroDivisionError("\033[31mError: Cannot divide by zero.\033[0m")
                result = num1 / num2
            else:
                raise ValueError("\033[31mError: Invalid operation\033[0m")
                break
        except ZeroDivisionError as e:
            print(f"{str(e)} Please enter the second number again: ")
            num2 = float(input("Enter the second number: "))
        except ValueError as e:
            print(f"{str(e)}")
            break
        # Print the result
        print("Result: ", result)
        break
    # Ask the user if they want to try again
    try_again = input("Do you want to try again? (Y/N):").lower()
    if try_again == "N":
        print("Okay, thank you!")
        break