import pandas as pd 
import numpy as np
from decimal import Decimal
from datetime import datetime
#make adult exercise equipment portion of places csv 
#extract
col_list = ["SiteName","Borough","EditDate", "point","Status","ClosureType"]
df = pd.read_csv("../input/exercise.csv", usecols=col_list) 
df.rename(columns = {'SiteName':'name'}, inplace = True)

#transform
df = df.replace(np.nan, 'N/A', regex=True)
df.insert(4, 'latitude', 1.0)
df.insert(5, 'longitude', 1.0)
df.insert(1, 'type', "ee")
for index, row in df.iterrows():
    #format date
    d = datetime.strptime(row["EditDate"], "%m/%d/%Y %H:%M:%S %p")
    df.at[index, "EditDate"] = d

    #construct name
    df.at[index, "name"] = row["name"] + " Exercise Equipment"

    #split point into lat and long
    temp = row["point"]
    temp = temp[7:len(temp)-1]
    pair = temp.split(' ')

    df.at[index, "latitude"] = pair[1]
    df.at[index, "longitude"] = pair[0]

df = df[["name", "type", "Borough","EditDate", "latitude","longitude","Status","ClosureType"]]
print(df)
    
#load
df.to_csv('../output/exercisenew2.csv', index=False)
