import numpy as np 
import pandas as pandas
import matplotlib.pyplot as plt 
import seaborn as sns

#  load a dataset
df =sns.load_dataset("tips")
#print(df.head())
n_df = df.select_dtypes(include = ['number'])
# correltion
correlation = n_df.corr()
#print(correlation)

# heatmap
sns.heatmap(n_df)
#plt.show()
#plt.savefig('heat.png')


# joint plot
sns.jointplot(x='tip',y ='total_bill',data =df, kind ='reg')
#plt.show()
#plt.savefig('joint3.png')



# pair plot 
sns.pairplot(df, hue ='sex')
#plt.show()
#plt.savefig('pairplot_hue.png')



#displot


sns.displot(df['tip'])
#plt.show()




# count plot 

sns.countplot(x = 'sex', data =df)
plt.show()

# bar plot 

sns.barplot(x='total_bill', y='sex', data = df)
plt.show()

# box plot 
sns.boxplot(x= 'sex',y ='total_bill', data = df, )
plt.show()



# agar box plot me he 3 featurs karne hai and 1 color se karna hai tub 

sns.boxplot(x='total_bill',y ='day', hue = 'smoker', data = df)
plt.show()

# violin plot
sns.violinplot(x="total_bill",y = "day", data = df, palette = 'rainbow')
plt.show()