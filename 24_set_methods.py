#UNION
s1 = {1,2,3,4}
s2={1,3,4,5,6,7}
print(s1.union(s2))# union matlb dono set ko add kar diya 
s1.update(s2)# ye function set ko update kar deta hai to dono ka union hua or fir update ho gaya 
print(s1,s2)

# INTERSECTION 

names1={"mike","harry","lisa","luke","dev"}
names2={"dev","harshit","anirudh","luke"}
print(names1.intersection(names2))#ye function do sets ke common yani intersection add karta hai
names1.intersection_update(names2)# isme interscetion kar ke update kar diya 
print(names1,names2)


#SYMMETRIC DIFFERENCE

# ISME SAMJHO KI UNION - INTERSECTION 



colour={"red","blue","green","pink","brown",}
colour2={"silver","gold","black","pink","brown"}
colour3=colour.symmetric_difference(colour2)# dono ko merge kiya or common hata diya 
print(colour3)


# disjoint set (matlb jub2 set me kuch common na ho )
# true and false return karega 

a={1,2,3,4,5}
b={6,7,8,9}
print(a.isdisjoint(b))

# sub set and super set 
# super set matlb main set 
#subset matlb super set ke kuch element se bana set

k ={1,2,3,4,5,6,7}
l={1,4,7,6}
print(l.issubset(k))