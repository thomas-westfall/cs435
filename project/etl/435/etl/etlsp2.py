import pandas as pd 
import numpy as np
from decimal import Decimal
from datetime import datetime

#make skatepark portion of places csv 
#extract
col_list = ["Name","Borough","EditDate", "polygon","Status","ClosureType"]
df = pd.read_csv("../input/skatepark.csv", usecols=col_list)

df.rename(columns = {'Name':'name'}, inplace = True)

#transform
df = df.replace(np.nan, '', regex=True)
df.insert(4, 'latitude', 1.0)
df.insert(5, 'longitude', 1.0)
df.insert(1, 'type', "sp")
for index, row in df.iterrows():

    #format datetime
    d = datetime.strptime(row["EditDate"], "%m/%d/%Y %H:%M:%S %p")
    df.at[index, "EditDate"] = d
    
    #get polygon data
    temp = row["polygon"]

    #remove unwanted characters
    temp = temp[10:len(temp)-2]
    temp = temp.replace(")", "")
    temp = temp.replace("(", "")

    #split list of pairs by commas
    pairlist = temp.split(',')

    #split each pair into two (lat and long)
    pairlist[0] = pairlist[0].split(" ")

    #start the sums of lat and long with the first pair
    sumlat = Decimal(pairlist[0][1])
    sumlong = Decimal(pairlist[0][0])
    for i in range(1, len(pairlist)):
        pairlist[i] = pairlist[i].split(" ")[1:] #remove leading space
        sumlat += Decimal(pairlist[i][1])
        sumlong += Decimal(pairlist[i][0])

    #calculate average lat and long
    lat = sumlat / len(pairlist)
    longg = sumlong / len(pairlist)
    df.at[index, "latitude"] = lat
    df.at[index, "longitude"] = longg
df = df[["name","type","Borough","EditDate", "latitude","longitude","Status","ClosureType"]]
print(df)
    
#load
df.to_csv('../output/skateparknew2.csv', index=False)
