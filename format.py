import pandas as pd

df = pd.read_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')
df["time"] = df['year'].astype(str) +"-"+ df["month"].astype(str)+"-"+ df["day"].astype(str)+"-"+ df["hour"].astype(str)
df.to_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')