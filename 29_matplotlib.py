import matplotlib.pyplot as pyt 
import numpy as np 
x= np.arange(0,10)
y = np.arange(11,21)



a = np.arange(40,50)
b= np.arange(50,60)


'''pyt.scatter(a,b,c='g')'''
y=x*x
pyt.plot(x,y,'g--')
pyt.xlabel('x axis')
pyt.ylabel('y axis')
pyt.title('Graph in 2D')
"""pyt.savefig('Test.png')# to save this image''' """
pyt.show()