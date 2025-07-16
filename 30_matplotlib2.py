# sub ploting 



import matplotlib.pyplot as pyt 
import numpy as np 


"""
x= np.arange(0,10)
y = np.arange(11,21)

pyt.subplot(2,2,1)
pyt.plot(x,y,'r--')
pyt.subplot(2,2,2)
pyt.plot(x,y,'g-*')
pyt.subplot(2,2,3)
pyt.plot(x,y,'bo')
pyt.subplot(2,2,4)
pyt.plot(x,y,'go')
pyt.show()




# sub ploting 



import matplotlib.pyplot as pyt 
import numpy as np 



x= np.arange(0,10)
y = np.arange(11,21)

pyt.subplot(2,2,1)
pyt.plot(x,y,'r--')
pyt.subplot(2,2,2)
pyt.plot(x,y,'g-*')
pyt.subplot(2,2,3)
pyt.plot(x,y,'bo')
pyt.subplot(2,2,4)
pyt.plot(x,y,'go')
pyt.show()






# CURVED FIG KE LIYE 
np.pi 
x= np.arange(0,4*np.pi,0.1)
y=np.sin(x)
pyt.title("Sine wave form")
pyt.show()# sub ploting 



import matplotlib.pyplot as pyt 
import numpy as np 



x= np.arange(0,10)
y = np.arange(11,21)

pyt.subplot(2,2,1)
pyt.plot(x,y,'r--')
pyt.subplot(2,2,2)
pyt.plot(x,y,'g-*')
pyt.subplot(2,2,3)
pyt.plot(x,y,'bo')
pyt.subplot(2,2,4)
pyt.plot(x,y,'go')
pyt.show()






# CURVED FIG KE LIYE 
np.pi 
x= np.arange(0,4*np.pi,0.1)
y=np.sin(x)
pyt.title("Sine wave form")
pyt.show()# sub ploting 



import matplotlib.pyplot as pyt 
import numpy as np 



x= np.arange(0,10)
y = np.arange(11,21)

pyt.subplot(2,2,1)
pyt.plot(x,y,'r--')
pyt.subplot(2,2,2)
pyt.plot(x,y,'g-*')
pyt.subplot(2,2,3)
pyt.plot(x,y,'bo')
pyt.subplot(2,2,4)
pyt.plot(x,y,'go')
pyt.show()







# CURVED FIG KE LIYE 
np.pi 
x= np.arange(0,4*np.pi,0.1)
y=np.sin(x)
pyt.title("Sine wave form")
pyt.plot(x,y)
pyt.show()



x=[2,8,10]
y=[11,16,9]
x2=[3,9,11]
y2=[6,15,7]
pyt.bar(x,y)
pyt.bar(x2,y2, color ='g')
pyt.title("Bar Graph")
pyt.xlabel("X axis")
pyt.ylabel("Y axis")
pyt.show()






# FOR MAKIN A HISTOGRAM

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
pyt.hist(a)
pyt.title("Histogram")
pyt.show()

"""


# PIE DIAGRAM USING MATPLOTLIB




labels='Python','C++','Ruby','Java'
sizes=[215,130,245,219]
colors="blue","yellowgreen","gold","lightgreen"
explode=(0.1,0,0,0)# explode 1st slice 

# plot
pyt.pie(sizes, explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow = True)
pyt.axis('equal')
pyt.show()