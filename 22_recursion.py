def factorial(n):
    if(  n==0 or n==1):
     return 1
    else:
       return n *factorial(n-1)


print(factorial(3))
# recursion is a process to breakdown the problem into smaller parts


# print fibonacci series

def fibo(n):
   if n<= 0 :
      return 0
   elif n==1:
      return 1
   else:
      return fibo(n-1)+ fibo(n-2)

terms = int(input("enter num of terms"))
for i in range(terms):
    print(fibo(i), end=" ")
