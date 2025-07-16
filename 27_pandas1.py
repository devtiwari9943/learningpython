import pandas as pd 
import numpy as np
'''
df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["Columns1","Columns2","Columns3","Columns4"])
print(df)


df = pd.read_csv('employee_records.csv')

'''

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header = None)
print(df.head())