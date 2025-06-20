# Question 1: Leap Year Checker
'''
a=int(input("enter any year "))
if a%4==0 and a%100!=0 or a%400==0:
    print(a,"is a leap year")
else:
    print(a," is not a leap year")
    '''


 #Question 2: Grade Calculator using if-elif-else
 
#Marks Range	Grade
#90 - 100	Grade A
#80 - 89	Grade B
#70 - 79	Grade C
#60 - 69	Grade D
#Below 60	Fail

'''

marks=int(input("enter your marks"))

if marks<60:
    print("you are fail")
elif marks>=60 and marks<=69:
    print("you have got grade D")
elif marks>=70 and marks<=79:
    print("you have got grade C")
elif marks>=80 and marks<=89:
    print("you have got grade B")
else:
    print("you have got grade A")
    '''



# question 3 triangle type 

#Take three numbers as input a, b, and c representing the sides of a triangle.

#👉 Use if-elif-else to:

#First check if it’s a valid triangle:

#Sum of any two sides must be greater than the third.

#If valid:

#All sides equal → Equilateral

#Two sides equal → Isosceles

#All sides different → Scalene
'''

a=int(input("enter first side "))
b=int(input("enter second side "))
c=int(input("enter third side "))
if((a+b)>c and (b+c)>a and (c+a)>b ):
    if a==b==c:
        print("this is an equilateral triangle")
    elif(a==b or b==c or c==a):
        print("this is an isosceles triangle")
    else:
        print("all sides are diff so this is an scalene triangle")
else:
    print("it can not be a triangle")
    '''



#Question 4: Character Classification
'''
a=input("enter any character ")
if a.isdigit():
    print(a, "is a digit")
elif a.isupper():
    print(a ,"is an upper case")
elif a.islower():
    print(a, "is a lower case")
else:
    print(a ,"is aspecial character")
    '''


#Question 5: Simple Calculator

a =int(input("enter your first no."))
b =int(input("enter your second no."))
o =(input("""enter the operation
          for addition enter 1
          for substraction enter 2
          for multiplication enter 3
          for division enter 4
          for remainder enter5"""))
if o=="1":
    print(a+b)
elif o=="2":
    print(a-b)
elif o=="3":
    print(a*b)
elif o=="4":
    print(a/b)
elif o=="5":
    print(a%b)
else:
    print("wrong input")