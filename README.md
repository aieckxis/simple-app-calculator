# Simple App Calculator
This Python program performs simple arithmetic operations on two numbers entered by the user. It handles invalid input, division by zero errors using a try-except block, and allows the user to continue performing operations or exit. If the user tries to divide by zero, the program raises a ZeroDivisionError and asks the user to enter the second number again.

## Usage
Using Command Prompt: 

1. Open the Start menu and search for "Command Prompt".
2. Click on "Command Prompt" to open the command prompt window.
3. Use the cd command to navigate to the directory containing the script file. For example, if the script file is located in the "Documents" folder, type: cd Documents
4. Type the command python script_name.py to run the script. Replace "script_name.py" with the actual name of the script file.
5. Press Enter to run the script.
6. The script will run and follow the prompts to input the operation and two numbers. User can then choose to try again or exit.

Alternatively, you can also run the script using the Python IDLE environment:

1. Open the Start menu and search for "Python".
2. Click on "Python" to open the Python IDLE environment.
3. Click on "File" at the top of the window and select "Open".
4. Navigate to the directory containing the script file and select it.
5. Click on "Run" at the top of the window and select "Run Module" or press the F5 key.
6. The script will run and follow the prompts to input the operation and two numbers. User can then choose to try again or exit.

## Code Explanation

<img width="600" alt="image" src="https://github.com/aieckxis/simple-app-calculator/assets/129574374/02f69c2f-0c77-4b2b-ba94-ad72abc5941e">

The program starts with an outer while loop that allows the user to perform multiple operations or exit. Within this loop, the user is prompted to enter an operation using the input function. The while loop ensures that the user has entered a valid operation before proceeding.

<img width="600" alt="image" src="https://github.com/aieckxis/simple-app-calculator/assets/129574374/f8b38f3a-47da-45a5-9a73-074bf2befd04">

After the operation is selected, the program prompts the user to enter two numbers. A nested while loop is used to ensure that the user enters valid input (numeric values). If the user enters invalid input, the program displays an error message and prompts the user to enter input again.

<img width="600" alt="image" src="https://github.com/aieckxis/simple-app-calculator/assets/129574374/26126e00-b563-4d9b-9e68-4941cf1eb843">

Next, the program performs the selected operation on the two numbers using if-elif statements. If the operation is division, the program checks if the second number is zero and raises a ZeroDivisionError if so. The program then displays an error message and asks the user to enter the second number again.

<img width="600" alt="image" src="https://github.com/aieckxis/simple-app-calculator/assets/129574374/947e76d2-03d5-4cd6-ba43-dbdcf05b0a0c">

Finally, the program displays the result of the operation, prompts the user to try again, and exits the program if the user chooses not to continue.

## Potential Improvements

## Conclusion


