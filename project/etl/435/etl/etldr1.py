import pandas as pd 
import numpy as np

#make dogruns csv 
#extract
col_list = ["PropertyName","SubPropertyName"]
df = pd.read_csv("../input/dogrun.csv", usecols=col_list) 
df.rename(columns = {'PropName':'propname', 'SiteName': 'subpropname'}, inplace = True)

#transform
df = df.replace(np.nan, 'N/A', regex=True)
i = 1289
df.insert(0, 'id', 1)
for index, row in df.iterrows():
    df.at[index, 'id'] = i
    i += 1
print(df)
#load
df.to_csv('../output/dogrunnew.csv', index=False)
