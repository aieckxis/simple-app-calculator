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
# Print the result
print(operation)
# Ask the user if they want to try again