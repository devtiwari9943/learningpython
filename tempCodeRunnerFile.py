a=input("enter any character")
if a.isdigit():
    print(a, "is a digit")
elif a.isupper():
    print(a ,"is an upper case")
elif a.islower():
    print(a, "is a lower case")
else:
    print(a ,"is aspecial character")