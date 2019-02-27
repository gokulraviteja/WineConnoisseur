import pandas as pd
data=pd.read_csv("data.csv")
cols=list(data.columns)
cols=cols[1:]
print(cols)
l=len(data)
for i in range(3):
    for j in cols:
        if(j=='description'):
            continue
        if(j=='price'):
            print(int(data.loc[i][j]),end=' || ')
            continue
        print(data.loc[i][j],end=' || ')
    print()


