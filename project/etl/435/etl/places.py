import pandas as pd 
import numpy as np

#make places csv 
pg = pd.read_csv("../output/playgroundnew2.csv") 
sp = pd.read_csv("../output/skateparknew2.csv") 
ee = pd.read_csv("../output/exercisenew2.csv") 
dr = pd.read_csv("../output/dogrunnew2.csv") 
af = pd.read_csv("../output/athfacnew2.csv") 
frames = [pg, sp, ee, dr, af]

df = pd.concat(frames)
df = df.replace(np.nan, 'N/A', regex=True)
df.rename(columns = {'Borough':'borough', 'EditDate': 'editdate', 'Status': 'status','ClosureType': 'closuretype'}, inplace = True)
print(df)

df.to_csv('../output/places.csv', index=False)
