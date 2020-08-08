import pandas as pd 
import numpy as np

#make playgrounds csv 
#extract
col_list = ["location","accessibilityLevel","rules"]
df = pd.read_csv("../input/playground.csv", usecols=col_list) 

#transform
df = df.replace(np.nan, '', regex=True)
i = 1
df.insert(0, 'place_id', 1)
for index, row in df.iterrows():
    df.at[index, 'place_id'] = i
    i += 1
    if(row["location"] == ""):
        df.at[index, "location"] = "Not Specified"
        
    if(row["accessibilityLevel"] == "Not Applicable" or row["accessibilityLevel"] == ""):
        df.at[index, "accessibilityLevel"] = "0"
    if("Level 1" in row["accessibilityLevel"]):
        df.at[index, "accessibilityLevel"] = "1"
    if("Level 2" in row["accessibilityLevel"]):
        df.at[index, "accessibilityLevel"] = "2"
    if("Level 3" in row["accessibilityLevel"]):
        df.at[index, "accessibilityLevel"] = "3"
    if("Level 4" in row["accessibilityLevel"]):
        df.at[index, "accessibilityLevel"] = "4"

    if(row["rules"] == ""):
        df.at[index, "rules"] = "Unknown"

df.rename(columns = {'accessibilityLevel':'accesslvl'}, inplace = True)
df = df[["place_id", "location", "accesslvl", "rules"]]
print(df)
#load
df.to_csv('../output/playgroundnew.csv', index=False)
