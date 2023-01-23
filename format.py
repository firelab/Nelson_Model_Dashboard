import pandas as pd

df = pd.read_feather('data/outputs/2021 Output/output_2021_8_12.ftr')
df.columns = df.columns.str.replace('precip ', 'precip')
df.to_feather('data/outputs/2021 Output/output_2021_8_12.ftr')