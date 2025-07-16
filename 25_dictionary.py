#dic ={"dev":"human","spoon" : "object"}
#print(dic["dev"])


info ={'name':'dev','age':21,'eligible':True}
print(info)#poori dict print karne ke liye 
print(info['name'])# key value print kare ke liye but agar is naam se koi key ni hai to error dega
print(info.get('name'))# key value print kare ke liye but agar is naam se koi key ni hai to error nhi dega  
print(info.keys())# keys print karne ke liye 
print(info.values())#values print karne ke liye

for key in info.keys():# saare keys print karne ke liye
    print(info[key]) 


print(info.items())# key value pair print karne ke liye 