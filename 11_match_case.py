# just like switch case in c and java 
# match case is similler to it but in this we dont have to write break statement , if the condition find true it will automatically  came out from the block




# example 1 calculator
# Prompt the user to input an operation
operation = input("""Choose an operation (+, -, *, /, %):
+ for addition
- for subtraction
* for multiplication
/ for division
% for remainder
Enter your choice: """)

# Take two numerical inputs
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Perform the chosen operation using match-case
match operation:
    case '+':
        print("Addition:", x + y)
    case '-':
        print("Subtraction:", x - y)
    case '*':
        print("Multiplication:", x * y)
    case '/':
        if y != 0:
            print("Division:", x / y)
        else:
            print("Error: Division by zero is not allowed!")
    case '%':
        if y != 0:
            print("Remainder:", x % y)
        else:
            print("Error: Division by zero is not allowed!")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /, or %.")
