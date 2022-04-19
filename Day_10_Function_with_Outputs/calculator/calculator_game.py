
from replit import clear

from cal_art import logo


# Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

# create a dictionary the key are +-*/ , the valus are names of the function
operations = {
    "+" : add,
    "-" : subtract,
    '*' : multiply,
    '/' : divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    # for循环去查找all the keys instead of values
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symble = input("Pick an operation from the line above: ")
        num2 = float(input('What is the second number?: '))
        # call the dictionary
        calculation_function = operations[operation_symble]
        answer = calculation_function(num1, num2)
        print(f"{num1}{operation_symble}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()




























