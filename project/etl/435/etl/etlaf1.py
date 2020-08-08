import pandas as pd 
import numpy as np

#make dogruns csv 
#extract
col_list = ["PropertyName","SubPropertyName", "PrimarySport", "FieldNumber", "Nets/Rims/Goals Removed", "SurfaceType"]
df = pd.read_csv("../input/athfac.csv", encoding= 'unicode_escape', usecols=col_list) 

df = df[["PropertyName","SubPropertyName", "PrimarySport", "FieldNumber", "Nets/Rims/Goals Removed", "SurfaceType"]]

df.rename(columns = {'PropertyName':'propname', 'SubPropertyName': 'subpropname', 'PrimarySport': 'primarysport', 'FieldNumber': 'fieldnumber', 'Nets/Rims/Goals Removed': 'netsremoved', 'SurfaceType': 'surfacetype'}, inplace = True)


#transform
df = df.replace(np.nan, 'N/A', regex=True)

i = 1374
df.insert(0, 'place_id', 1)
for index, row in df.iterrows():
    df.at[index, 'place_id'] = i
    i += 1
    nonets = df.at[index, "netsremoved"]
    if(nonets and str(nonets) != "N/A"):
        df.at[index, "netsremoved"] = "1"
    else:
        df.at[index, "netsremoved"] = "0"
    # if(not df.at[index, "netsremoved"]):
    #     df.at[index, "netsremoved"] = "0"
    # if(df.at[index, "netsremoved"] == "N/A"):
    #     df.at[index, "netsremoved"] = "0"
print(df)
#load
df.to_csv('../output/athfacnew.csv', index=False)
