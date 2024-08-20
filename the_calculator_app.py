# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
def add(number1, number2): #created an addition function
    newnumber=number1 + number2
    return newnumber

def sub(number1, number2): #created a subtraction function
    newnumber=number1 - number2
    return newnumber

def mul(number1, number2): #created a multiplication function
    newnumber=number1 * number2
    return newnumber

def div(number1, number2): #created a division function
    newnumber=number1 / number2
    return newnumber

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
print("This program will perform basic math functions.")

while True: #added a while true infinite loop so the user could repeat for different functions more easily while providing an exit in the "quit" option   
    user_operation = input ("Please enter the operation you would like to perform or type 'quit' to exit.\n(addition/subtraction/multiplication/division): ").lower #asked for user input of what operation to perform converted to lowercase to account for case issues
    if user_operation() == "quit": #provided a "quit" option to exit the loop in an if statement
        break
    elif user_operation() == "addition" or user_operation() == "subtraction" or user_operation() == "multiplication" or user_operation() == "division": #used conditional if statements to allow input of numbers only if the requested operation is valid
        number1 = float(input ("What is the first number you would like perform the operation on: ")) #requested input of numbers and made them floats for more flexible calculations           
        number2 = float(input ("What is the second number you would like use in the operation: "))
        if user_operation() == "addition": #addition code
            result = add(number1,number2)
            print(number1, "+", number2, "=", result)
        elif user_operation() == "subtraction": #subtraction code
            result = sub(number1,number2)
            print(number1, "-", number2, "=", result)
        elif user_operation() == "multiplication": #multiplication code
            result = mul(number1,number2)
            print(number1, "*", number2, "=", result)
        elif user_operation() == "division": #division code w/ if-else statement used to see if a DivisionByZero Error would occur adding a path to give user feedback as to the undefined result and how to proceed
            if number2==0:
                print("Result is undefined because you divided by 0.\nPlease try inputing a different second number.")
                continue
            else: 
                result = div(number1,number2)
                print(number1, "/", number2, "=", result)
    else:
        print("User input does not match available operations. Please try again...")

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
# inserted an if-else statement to the division code to handle if the user input creates an instance of division by 0