#nested if else is for condition under condition as shown in below program

num=int(input("enter any digit "))

if(num<0):
    print ("num is negative")
elif(num>0):
    if(num<=10):
        print("num is between 1 -10")
    elif(num>10 and num <=20):
        print("num is between 11 - 20")
    else:
        print("num is greaater than 20")
else:
    print("num is zero")