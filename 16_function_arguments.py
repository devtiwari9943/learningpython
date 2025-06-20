
# function
def average (a,b,c):# here a,b,c are the arguments 
    print ("the average is ", (a+b+c)/2)



average(5,7,9)
#In Python, function arguments are the values you pass to a function when you call it. These arguments provide the input data for the function to operate on. Python allows several types of arguments, offering flexibility for different use cases.

#Types of Function Arguments



#Positional Arguments
#These are the most common and must be passed in the same order as the parameters in the function definition.

#Example


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Dev", 21)  # Output: Hello Dev, you are 21 years old.




#Default Arguments
#You can assign a default value to a parameter. If the argument is not provided, the default value will be used.

#eample


def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Dev")         # Output: Hello Dev, you are 18 years old.
greet("Dev", 21)     # Output: Hello Dev, you are 21 years old.



#Keyword Arguments
#You can explicitly specify which parameter you're assigning a value to, regardless of the order.

#Example


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=21, name="Dev")  # Output: Hello Dev, you are 21 years old.




# args arfuments 


#What is *args?

#*args allows a function to accept any number of positional arguments.
#These arguments are packed into a tuple (a collection of items, like a list, but immutable).
#Example of *args:


def add_numbers(*args):
    total = sum(args)  # Add all numbers in the tuple
    print(f"Numbers: {args}, Sum: {total}")

add_numbers(1, 2, 3, 4)  # Output: Numbers: (1, 2, 3, 4), Sum: 10
add_numbers(10, 20)      # Output: Numbers: (10, 20), Sum: 30
add_numbers()            # Output: Numbers: (), Sum: 0


#Key Points:

#You can pass as many positional arguments as you want.
#nb Inside the function, args is treated as a tuple.


#kwargs arguments

#What is **kwargs?
#**kwargs allows a function to accept any number of keyword arguments (arguments with names).
#These arguments are packed into a dictionary (key-value pairs).


#Example of **kwargs:

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Dev", age=21, city="Lucknow")
# Output:
# name: Dev
# age: 21
# city: Lucknow

describe_person(name="Alice", hobby="Coding")
# Output:
# name: Alice
# hobby: Coding


#Key Points:

#You can pass as many keyword arguments as you want.
#Inside the function, kwargs is treated as a dictionary.