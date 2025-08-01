# if we want to creat a new list of using previous list in which new list elements are the the sqared of the previous list 



# normal way 
lst1=[]
def lst_square(lst):
    for i in lst :
        lst1.append(i*i)
    return lst1
a=lst_square([1,2,3,4,5,6,7,8,9])
print (a)


# this sollution is long and is we want to reduce the time complexity

# now we will use list comprehension 
lst = [1,2,3,4,5,6,7,8,9]
a = [i*i for i in lst] # using this way it will reduce time and space 
print (a)



# in this we can apply like this 
b= [i*i for i in lst if i%2==0] # using this way it will reduce time and space 
print (b)