#list

marks=[1,2,3,4,5,6,"dev"]# we can add in list afterwords also  and we can make list with containing different data types elements
 
print(type(marks))
print(marks)
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[0])
print(marks[5])
print(marks[6])



# OUTPUT
#<class 'list'>
#[1, 2, 3, 4, 5, 6]
#2
#3
#4
#5
#1
#6
#dev

if 3 in marks:# for checking that this element is in list or not 
    print("yes")
else:
    print("no")

# same thing applies in string as well
if "de" in "dev":
    print("yes")
else:
    print("no")