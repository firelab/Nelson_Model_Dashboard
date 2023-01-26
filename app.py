import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Instantiation of the app and supression of startup exceptions
# This is done to account for my multiple app.callbacks on each page
app = dash.Dash(__name__, suppress_callback_exceptions=True)

#This is the first layer of HTML elements
app.layout = html.Div(children=[
    html.H1(children='Blue Mountain RAWS Nelson Model Test Results', style={'text-align': 'center'}),

    html.Br(), html.Br(),
            html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': '2021 January - August', 'value': '2021JA'},
                    {'label': '2021 August - Decemeber', 'value': '2021AD'},
                    {'label': '2022 April - September', 'value': '2022AS'},
                    {'label': '2022 June - September', 'value': '2022JS'},
                    {'label': 'Synthetic Dry-Wet-Dry', 'value': 'DWD'},
                    {'label': 'Synthetic Wet-Dry-Wet', 'value': 'WDW'},
                    ],
                value='2021JA',
                style={"width": "60%"}),
            
            html.Div(dcc.Graph(id='map')),
])    
@app.callback(
    Output('map', 'figure'),
    [Input(component_id='dropdown', component_property='value')],
)
def select_graph(value):
    if value == '2021JA':
        check = True
        df = pd.read_feather('data/outputs/2021 Output/2021_1_8_Mean.ftr')
        df2 = pd.read_feather('data/outputs/2021 Output/2021_1_8_Median.ftr')
        df3 = pd.read_feather('data/outputs/2021 Output/2021_1_8_Outer.ftr')
        title = '2021 Nelson Model All January - August vs Precipitation'

    elif value == '2021AD':
        check = True
        df = pd.read_feather('data/outputs/2021 Output/2021_8_12_Mean.ftr')
        df2 = pd.read_feather('data/outputs/2021 Output/2021_8_12_Median.ftr')
        df3 = pd.read_feather('data/outputs/2021 Output/2021_8_12_Outer.ftr')
        title = '2021 Nelson Model All August - December vs Precipitation'
    
    elif value == '2022AS':
        check = True
        df = pd.read_feather('data/outputs/April-Sept Output/output_mean_AS.ftr')
        df2 = pd.read_feather('data/outputs/April-Sept Output/output_median_AS.ftr')
        df3 = pd.read_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')
        title = '2022 Nelson Model All April - September vs Precipitation'

    elif value == '2022JS':
        check = True
        df = pd.read_feather('data/outputs/June-Sept Output/output_mean_JS.ftr')
        df2 = pd.read_feather('data/outputs/June-Sept Output/output_median_JS.ftr')
        df3 = pd.read_feather('data/outputs/June-Sept Output/output_outer_JS.ftr')
        title = '2022 Nelson Model All June - September vs Precipitation'

    elif value == 'DWD':
        check = True
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_mean.ftr')
        df2 = pd.read_feather('data/outputs/DWD output/output_syn_dwd_median.ftr')
        df3 = pd.read_feather('data/outputs/DWD output/output_syn_dwd_outer.ftr')
        title = 'Synthetic Dry-Wet-Dry All vs Precipitation'

    elif value == 'WDW':
        check = True
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_mean.ftr')
        df2 = pd.read_feather('data/outputs/WDW output/output_syn_wdw_median.ftr')
        df3 = pd.read_feather('data/outputs/WDW output/output_syn_wdw_outer.ftr')
        title = 'Synthetic Wet-Dry-Wet All vs Precipitation'

    else:
        select_graph('2021JA')   
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=df['time'], y=df['precip'], name="Precip (cm)"),
        secondary_y=True
    )
    fig.update_traces(width=5, opacity=0.5)
    fig.add_trace(
        go.Scatter(x=df['time'], y=df['1hrfm'], name="Mean 1hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df['time'], y=df['10hrfm'], name="Mean 10hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df['time'], y=df['100hrfm'], name="Mean 100hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df['time'], y=df['1000hrfm'], name="Mean 1000hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df2['time'], y=df2['1hrfm'], name="Median 1hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df2['time'], y=df2['10hrfm'], name="Median 10hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df2['time'], y=df2['100hrfm'], name="Median 100hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df2['time'], y=df2['1000hrfm'], name=" Median 1000hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df3['time'], y=df3['1hrfm'], name="Outer 1hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df3['time'], y=df3['10hrfm'], name="Outer 10hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df3['time'], y=df3['100hrfm'], name="Outer 100hrfm", opacity= .6),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(x=df3['time'], y=df3['1000hrfm'], name="Outer 1000hrfm", opacity= .6),
        secondary_y=False
    )

    fig.update_yaxes(title_text="<b>Nelson Model</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Precip (cm)</b>", secondary_y=True)
    fig.update_xaxes(title_text="<b>Date and Time</b>")
    fig.update_layout(title="<b>"+ title+"</b>")

    return fig      

# This sets the server ip and port. As well as enables debugging, which is needed to force reload when feather files change
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port = '8050', debug=True)
