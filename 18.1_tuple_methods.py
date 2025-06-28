#MANIPULATING TUPLES (INDIRECTLY)

'''

countries=("spain","Italy","India","England","Germany")#main tuple
temp=list(countries)#converting tuple into list
temp.append("Russia")#add item
temp.pop(3)#removing item
temp[2]="Finland"#replacing item
countries=tuple(temp)#converting back list to tuple
print(countries)
'''

# we can add 2 tuple but the original 2 tuple will not be change , a third tuple will be formed
'''
num=(1,2,3,4,5)
alpha=("a","b","c","d")
alphanum=num+alpha
print(alphanum)
'''


tup=(1,2,3,4,5,4,5,4,2,6,7,9,4,57,8,5,23,1,3,5,6,7,8,9,98,7,6,5,4,3,)
#res=tup.count(9)                    #counting how many times an element has come in tuple
#print("count of 9 in tup is:",res)


# INDEXING SAME HOTI HAI LIST KI TRAH 



# agar tuple ke ander kuch part me find karna hai ki kisi  element ki index kya hai tub
# res=tup.index(element , start from ,end at)
res =tup.index(5,4,10)
print(res)