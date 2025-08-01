# this is use to filter 



def even (num):
    if num%2==0:
        return True

lst = [1,2,3,4,5,6,7,8,9]

a= list(filter(even,lst))# this function filters the  jo bhi given function hoga usko choddh ke baki sub hata dega  , iterable  
# filter ke ander labda use kar sakte hai
print(a)



 