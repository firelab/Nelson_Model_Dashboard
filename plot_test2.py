import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_feather('data/outputs/2021 Output/output_2021_8_12.ftr')

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(x=df['time'], y=df['precip'], name="Precip (cm)"),
    secondary_y=True
)
fig.update_traces(width=5)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['1hrfm'], name="1hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['10hrfm'], name="10hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['100hrfm'], name="100hrfm"),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=df['time'], y=df['1000hrfm'], name="1000hrfm"),
    secondary_y=False
)
fig.update_yaxes(title_text="<b>Nelson Model</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Precip (cm)</b>", secondary_y=True)
fig.update_xaxes(title_text="<b>Date and Time</b>")
fig.update_layout(title="<b>Nelson Model vs Precipitation</b>")
fig.show()