def even_or_odd (num):
    if num%2 == 0 :
        return  "{} is even ".format(num)
    else :
        return " {} is odd".format(num)


a =even_or_odd(45)
print(a)




 # for any list 
 # we will use map function
lst = [1,2,3,4,5,6,7,8,9,0,]
b=list(map(even_or_odd,lst))# first is function name and second is iterable
print (b)
