import pandas as pd 
import numpy as np

#make adult excercise equipment csv 
#extract
col_list = ["PropName","SiteName"]
df = pd.read_csv("../input/exercise.csv", usecols=col_list) 
df.rename(columns = {'PropName':'propname', 'SiteName': 'subpropname'}, inplace = True)

#transform
df = df.replace(np.nan, 'N/A', regex=True)
i = 1063
df.insert(0, 'id', 1)
for index, row in df.iterrows():
    df.at[index, 'id'] = i
    i += 1
print(df)
#load
df.to_csv('../output/exercisenew.csv', index=False)
