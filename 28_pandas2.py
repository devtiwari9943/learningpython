import pandas as pd
import numpy as np 
'''
data ='{"employee_name": "Dev","email":"dev@gmail.com","job_profile":[{"title1 ":"Team lead","titile2":"Sr. developer"}]}'
a = pd.read_json(data)
print(a)
'''
url ='https://companiesmarketcap.com/inr/most-profitable-companies/'
dfs= pd.read_html(url)
print(dfs)