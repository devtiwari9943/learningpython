# take a string input and print the last 4 character using slicing
'''a = input("enter your full name :")
print(a[len(a)-4:len(a)])


#OR both the ways are correct

a = input("Enter your full name: ")
print(a[-4:])'''





 #Question 2:
#Take a string input and print it without the first 2 and last 2 characters using slicing.

'''
a =input("enter your name :")
print(a[2:-2])

'''

#🔹 Question 3:
#Given a string, print every third character starting from the first character.
'''
a =input("enter your name :")
print(a[::3])

#OR 


a =input("enter your name :")
print(a[:len(a):3])
'''




#🔹 Question 4:
#Reverse a string using slicing without using any loops or built-in reverse functions.

'''
a =input("enter your name :")
print(a[::-1])
'''

#🔹 Question 5:
#Take a string input and check if the string reads the same forwards and backwards (i.e., if it's a palindrome) using slicing only.
a = input("enter your string :")
b=a[::-1]
print(a==b)