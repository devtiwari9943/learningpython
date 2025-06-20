#QUESTION print num 1 to 10



#for i in  range(11):
#    print (i)



# QUESTION sum of all the num from 1 to 100


#i=0
#sum =0
#while(i<=100):
#    sum = sum +i
#    i =i+1
#print(sum)


# SOLTION OF same question using for loop


#total = 0
#for i in range(1, 101):
#    total += i
#print(total)





# QUESTION PRINT EACH HARACTER IN A STRING"hello"


'''
s = "hello"
for i in s :
    print(i)
'''



# PRINT EVEN NUM IN A RANGE 1 TO 20


'''
for i in range(0,21):
    if i %2==0:
        print(i)
'''



# LIST OF SQUARES 
'''num=[1,2,3,4,5]
for i in num:
    print(i**2)'''


# same question to print in list form 
'''numbers = [2, 4, 6, 8]
squares = []

for num in numbers:
    squares.append(num**2)#In Python, .append() is a method used to add an element to the end of a list.

print(squares)
'''





#FIND MAX IN A LIST 
'''a =[1,2,3,4,5,66,77,55,45,34,23,45,67,87,98,94,44,55,62,6,]
max=a[0]
for i in a :
    if i>max:
        max=i
print(max)
'''




#LOOP FOR PRINTING TABLE OF 5
'''
for i in range(1,11):
    print("5 X",i,"=",5*i)
    '''




#CHECK THE GIVEN NUM IS PRIME OR NOT 
'''

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


num =int(input("enter any num  "))
if is_prime(num):
    print( num ," is prime")
else:
    print(num ,"is not prime ")
    '''




# PATTERN QUESTIONS
'''
 Print this pattern:
markdown
Copy
Edit
* * * *
* * * *
* * * *
* * * *
* * * * 


'''
'''
for i in  range(4):
    for j in range (4):
        print("*",end=" ")
    print()
'''


#PATTERN 2
'''
*
* *
* * *
* * * *
* * * * *
'''
'''

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    '''


#PATTERN3
'''

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    '''


#PATTERN 4
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

'''
n =int(input("enter num. of rows "))
for i in range(n):
    for s in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
'''



#PATTERN5 

'''
        *        
      * * *      
    * * * * *    
  * * * * * * *  
* * * * * * * * *
'''
'''
n=5
for i in range(n):
    for s in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
    '''

'''
🔶 Q6: Inverted Pyramid of Stars
For n = 5, print this pattern:

markdown
Copy
Edit
* * * * * * * * * 
  * * * * * * *  
    * * * * *  
      * * *  
        *  
        '''

n=5
for i in range(n):
    for s in range(n-i-1):
        print(" ",end=" ")
    for j in range(n*2-(i+1)):
        print("*",end=" ")
    print()