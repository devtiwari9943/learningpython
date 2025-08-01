import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
# EDA ->  Exploratory data analysis 

# load a data set
train = pd.read_csv('titanic.zip')
#print (train.head())

#  To check the missing deta or null values

print (train.isnull()) # it will show true and false whichever data is null it will show null feature wise  but ye poora data set use nhi karega it will skip beech me se plenty of data set 


# so now we will use heat map to show null values 

sns.heatmap(train.isnull(),yticklabels = False , cmap = 'viridis')# here train.isnull is the dataset , ytick me fales kiya taki y axis ka markings na aai 
# isi me agar hum cbar= False likh denge to right me jo color grade marking hai vo lane ya hatne ke liye hoti hai and false menans nhi lana hai 
# ye heat map sirf density bata raha hai 
plt.show() 


#  isi data ko acche se visualise karne ke liye we will use count plot 


sns.set_style('whitegrid')# background me white grid lane ke liye 
sns.countplot(x='Survived', data= train)
plt.show()


# aub isi ko gender wise alag alag dikhana hai ki kitne males bache kitni females so we will use hue



sns.set_style('whitegrid')# background me white grid lane ke liye 
sns.countplot(x='Survived', hue ='Sex',data= train , palette ='RdBu_r')
plt.show()



# aub passenger class ke hisab se devide karan hai ki kitni doobe kitne bache 

sns.set_style('whitegrid')# background me white grid lane ke liye 
sns.countplot(x='Survived', hue ='Pclass',data= train , palette ='rainbow')
plt.show()


#   aub age wise batana hai ki is  dataset ke hisab se titanic me kis range ki age vale passengers the 

sns.displot(train['Age'].dropna(),kde=False,color= 'darkgreen',bins= 40) # .dronap ka matlb hai ki isme null values thi usko skip karne ke liye , kde = false matlb kernal density ali line ko hatane ke liye 
plt.show()

# aub hume siblings and spouse ka count dekhne ke liye count plot se lete hai 


sns.countplot(x='SibSp',data = train,palette='rainbow')
plt.show()

# box plot


sns.boxplot(x='pclass',y='Age', data =train , palette ='winter')
plt.show()