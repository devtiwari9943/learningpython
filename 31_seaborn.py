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

sns.countplot('sex', data = df)
plt.show()