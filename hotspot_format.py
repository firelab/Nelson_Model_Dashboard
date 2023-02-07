import pandas as pd

df = pd.read_feather('data/outputs/2021 Output/2021_8_12_Outer.ftr')
df2 = pd.read_csv('data/modis_2021_Blue_Mountain.csv')
df3 = pd.read_csv('data/viirs-snpp_2021_Blue_Mountain.csv')

df4 = df.loc[df['hour']== 14]
df4['modis'] = 0
df4['viirs'] = 0

for index, row in df4.iterrows():
    year = str(row['year'])
    if row["month"] < 10:
        month = "0"+ str(row["month"])
    else:
        month = str(row["month"])
    if row["day"] < 10:
        day = "0"+ str(row["day"])
    else:
        day = str(row["day"])
    date = year +"-"+ month +"-"+ day 
    modis = df2['Date'].str.contains(date).sum()
    viirs = df3['Date'].str.contains(date).sum()
    df4.at[index,'modis'] = modis
    df4.at[index,'viirs'] = viirs

df4.to_csv('data/outputs/2021 Output/hotspot/HS_2021_8_12_Outer.csv')