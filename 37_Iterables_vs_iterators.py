# iterables 
lst = [1,2,3,4,5,6]
for i in lst:
   print(i)


# now what is iterators
# ANS --> an iterator is an object that allows you to traverse through all the elements of a collection (like a list or tuple) one element at a time.
a=iter(lst)
print (next(a))# this is the one way 
print (next(a))
print (next(a))
# it will store one by one 
