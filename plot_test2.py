import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_feather('data/outputs/April-Sept Output/output_mean_AS.ftr')
df2 = pd.read_feather('data/outputs/April-Sept Output/output_median_AS.ftr')
df3 = pd.read_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')
title = '2022 Nelson Model All April - September vs Precipitation'

print(df['time'])
print(df2['time'])
print(df3)

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df['time'], y=df['precip'], name="Precip (cm)"),
    secondary_y=True
)
fig.update_traces(width=5, opacity=0.6)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['1hrfm'], name="Mean 1hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['10hrfm'], name="Mean 10hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['100hrfm'], name="Mean 100hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['1000hrfm'], name="Mean 1000hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df2['time'], y=df2['1hrfm'], name="Median 1hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df2['time'], y=df2['10hrfm'], name="Median 10hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df2['time'], y=df2['100hrfm'], name="Median 100hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df2['time'], y=df2['1000hrfm'], name=" Median 1000hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df3['time'], y=df3['1hrfm'], name="Outer 1hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df3['time'], y=df3['10hrfm'], name="Outer 10hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df3['time'], y=df3['100hrfm'], name="Outer 100hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df3['time'], y=df3['1000hrfm'], name="Outer 1000hrfm"),
    secondary_y=False
)

fig.update_yaxes(title_text="<b>Nelson Model</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Precip (cm)</b>", secondary_y=True)
fig.update_xaxes(title_text="<b>Date and Time</b>")
fig.update_layout(title="<b>"+ title+"</b>")

fig.show 