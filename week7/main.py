import pandas as pd
with open('/Users/olena/kse/kse_pb/week7/flights.csv','r') as f:
    read_csv=f.read
df=pd.read_csv('/Users/olena/kse/kse_pb/week7/flights.csv')
indexes=list(df.index)
df.reset_index


