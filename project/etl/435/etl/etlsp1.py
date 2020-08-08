import pandas as pd 
import numpy as np

#make skateparks csv 
#extract
col_list = ["PropertyName","SubPropertyName"]
df = pd.read_csv("../input/skatepark.csv", usecols=col_list) 
df.rename(columns = {'PropertyName':'propname', 'SubPropertyName': 'subpropname'}, inplace = True)

#transform
df = df.replace(np.nan, 'N/A', regex=True)
i = 1027
df.insert(0, 'place_id', 1)
for index, row in df.iterrows():
    df.at[index, 'place_id'] = i
    i += 1
print(df)
#load
df.to_csv('../output/skateparknew.csv', index=False)
