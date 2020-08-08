import pandas as pd 
import numpy as np
from decimal import Decimal
from datetime import datetime
#make playgrounds portion of places csv 
#extract
col_list = ["name","Borough","EditDate", "point","Status","ClosureType"]
df = pd.read_csv("../input/playground.csv", usecols=col_list) 

#transform
df = df.replace(np.nan, '', regex=True)
df.insert(4, 'latitude', 1.0)
df.insert(5, 'longitude', 1.0)
df.insert(1, 'type', "pg")

for index, row in df.iterrows():
    #print(row["EditDate"])
    d = datetime.strptime(row["EditDate"], "%m/%d/%Y %H:%M:%S %p")
    df.at[index, "EditDate"] = d

    temp = row["point"]
    temp = temp[7:len(temp)-1]
    pair = temp.split(' ')
    #print(pair)
    df.at[index, "latitude"] = pair[1]
    df.at[index, "longitude"] = pair[0]
df = df[["name","type","Borough","EditDate", "latitude","longitude","Status","ClosureType"]]
print(df)
    
#load
df.to_csv('../output/playgroundnew2.csv', index=False)
