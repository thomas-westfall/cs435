import pandas as pd 
import numpy as np
from decimal import Decimal
from datetime import datetime

#make dogruns portion of places csv 
#extract
col_list = ["Name","Borough","EditDate", "polygon","Status","ClosureType"]
df = pd.read_csv("../input/dogrun.csv", usecols=col_list)

df.rename(columns = {'Name':'name'}, inplace = True)
#transform
df = df.replace(np.nan, '', regex=True)
df.insert(4, 'latitude', 1.0)
df.insert(5, 'longitude', 1.0)
df.insert(1, 'type', "dr")

for index, row in df.iterrows():
    #print(row["EditDate"])
    d = datetime.strptime(row["EditDate"], "%m/%d/%Y %H:%M:%S %p")
    df.at[index, "EditDate"] = d
    
    sumlat = 0.0
    sumlong = 0.0
    temp = row["polygon"]
    temp = temp[10:len(temp)-2]
    #print(temp)
    temp = temp.replace(")", "")
    temp = temp.replace("(", "")
    pairlist = temp.split(',')

    pairlist[0] = pairlist[0].split(" ")
    sumlat = Decimal(pairlist[0][1])
    sumlong = Decimal(pairlist[0][0])
    for i in range(1, len(pairlist)):
        pairlist[i] = pairlist[i].split(" ")[1:]
        sumlat += Decimal(pairlist[i][1])
        sumlong += Decimal(pairlist[i][0])
    lat = sumlat / len(pairlist)
    longg = sumlong / len(pairlist)
    df.at[index, "latitude"] = lat
    df.at[index, "longitude"] = longg
df = df[["name","type","Borough","EditDate", "latitude","longitude","Status","ClosureType"]]
print(df)
    
#load
df.to_csv('../output/dogrunnew2.csv', index=False)
