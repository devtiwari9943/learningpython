# even or odd
'''

a =int(input("enter any number :"))
if (a%2==0):
    print("no is even" ,a)
else:
    print("no. is odd" ,a)
    '''


#🔹 Question 2:
#Take a number input and check if it’s positive, negative, or zero using if-elif-else.


'''
a =int(input("enter any number :"))
 
if(a>0):
    print (a, "is positive")
elif(a<0):
    print(a,"is negative")
else:
    print(a ," is zero")
    '''

# Question 3:
#Check if a person is a Minor, Adult, or Senior Citizen based on their age.


'''
age =int(input("enter your age :"))

if age<18:
    print("you are minor")
elif age >=18 and age<=60:   # or  18 <= age <= 60:
    print("you are an adult")
else:
    print("you are senior citizen")
    '''


#question 4 
#Check if the entered character is a vowel or consonant (assume lowercase input).

'''
a = input("enter any alphabet: ")

if a in 'aeiouAEIOU':
    print(a, "is a vowel")
else:
    print(a, "is a consonant")
'''


#Question 5:
# Take two numbers and print which one is greater.


a=int(input("enter any num."))
b=int(input("enter any num."))
if a>=b:
    print(a, "is greater")
else:
    print(b , "is greater")
