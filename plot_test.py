import plotly.express as px
import pandas as pd

df = pd.read_feather('data/outputs/April-Sept Output/output_mean_AS.ftr')

fig = px.bar(df, x='time', y='precip')
fig.update_traces(width=5)
fig.add_scatter(x=df['time'], y=df['1hrfm'], opacity=0.5, line=dict(
                width=2
            ))
fig.add_scatter(x=df['time'], y=df['10hrfm'], opacity=0.5, line=dict(
                width=2
            ))
fig.add_scatter(x=df['time'], y=df['100hrfm'], opacity=0.5, line=dict(
                width=2
            ))
fig.add_scatter(x=df['time'], y=df['1000hrfm'], opacity=0.5, line=dict(
                width=2
            ))
fig.show()