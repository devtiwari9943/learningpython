#jump index in list 
marks = [1,9,6,8,9,22,34,4,5,23,7,2,9,76,45,3,98,34,23,12]
#print(marks[0:19:2])
# jump is (in slicing part if there is a third num after(:)it will known as jupm value )
# third num  me jitni bhi value hogi utna skip hoga suppose 1,2,3,4,5 hai or jump me 2 hai to print karne pe 1,3,5 aaiga


'''
marks.append(21)    #list ke end me element add karne ke liye 
print(marks)
'''
'''
marks.sort()   #list sort karne ke liye
print(marks)
'''
'''
marks.sort( reverse=True)   #for printing reverse sorting
print(marks) 
'''
'''

marks.reverse()   # to reverse the list
print(marks)
'''
'''
print(marks.index(6))   #ito find index of an element
'''
'''

m=marks.copy() #ek list ko copy karne ke liye or new list me changes karne ke liye 
m[0]=32
print(m)
'''



'''
marks.insert(index,element)     # kisi bhi index pe element add karne ke liye
marks.insert(0,456)
print(marks)
'''
'''
m=[9000 ,3444,5666,7644,24]
marks.extend(m)    #kisi bhi list ko kisi doosri list ke end  me add karne ke liye 
print(marks)
'''
'''
m=[456,644,456,433]
k=marks+m     #2 list ko add karne ke liye without changing original lists 

print (k)
'''


