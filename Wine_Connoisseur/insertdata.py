import pandas as pd
import numpy as np
from wine.models import winedata
data=pd.read_csv("data.csv")
cols=list(data.columns)
cols=cols[1:]
print(cols)
l=len(data)

for i in range(l):
    arr=[]
    for j in cols:
        if(np.nan==(data.loc[i][j])):
            arr.append("not-available")
        else:
            arr.append(data.loc[i][j])
    tt=winedata(country=arr[0],description=arr[1],designation=arr[2],points=arr[3],price=arr[4],province=arr[5],region_1=arr[6],region_2=arr[7],variety=arr[8],winery=arr[9])
    tt.save()
