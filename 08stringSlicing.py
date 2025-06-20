# STRING SLICING
# now it is a way to take out data from between of the string 
# example 
name = "dev,tiwari "
print(name[0:5])#including 0 excluding 5 because it will start from the first given index and the last given index does not count (like n-1 position )
#out ut is devti
#print(name[:5]) it will automatically take it as the 0
#print(name[1:])now here it will take it as a length of the string
#print(name([-4:-2]))now here it will act as length of the string minus 4, length of string minus 2




# HERE IS A CATCH 
# there will given an error if we give opposit number means 
#[4:2] or [-1:-3]








# we can print the length of a string
name2="dev tiwari"
print(len(name2))