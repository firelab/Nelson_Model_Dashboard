import pandas as pd

df = pd.read_csv('data/outputs/2021 Output/2021_8_12_Outer.csv')
df2 = pd.read_csv('data/outputs/2021 Output/precip_2021_8_12.csv')


#adding the precip columns
df["precip"] = df2['0.0']

# creating the time columns
df["time"] = df['year'].astype(str) +"-"+ df["month"].astype(str)+"-"+ df["day"].astype(str)+"-"+ df["hour"].astype(str)
df.to_feather('data/outputs/2021 Output/2021_8_12_Outer.ftr')
