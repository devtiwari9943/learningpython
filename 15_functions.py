# function (it helps to combine a set of log program into one single line )
#def is a keyword which is use to write a function




# like the is a program where manu users can give there input and we have to find greatest among them , geometric mean etc




# the function starts here 
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print (mean)

# second function 
def isGreater(a,b):
    if(a>b):
        print("first num is greater")
    else:
        print("second num is greater")

def isLesser(a,b):#in this function i am only writing the marameters and declaring them i will further write the main body of this function 
    pass #(PASS ) is the keyword we have to use if there is a incomplete function is it is not there it will show as error



#now the main program begins 
a= 9
b=8
# this is the calling of the function
isGreater(a,b)
calculateGmean(a,b)

c=7
d=12
#calling of the functions
isGreater(c,d)
calculateGmean(c,d)