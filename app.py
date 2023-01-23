import pandas as pd
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Instantiation of the app and supression of startup exceptions
# This is done to account for my multiple app.callbacks on each page
app = dash.Dash(__name__, suppress_callback_exceptions=True)

#This is the first layer of HTML elements
app.layout = html.Div(children=[
    html.H1(children='Nelson Model Test Results', style={'text-align': 'center'}),

    html.Br(), html.Br(),
            html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': '2021 January - August', 'value': '2021JA'},
                    {'label': '2021 August - Decemeber', 'value': '2021AD'},
                    {'label': '2022 April - September Mean', 'value': '2022ASMean'},
                    {'label': '2022 April - September Median', 'value': '2022ASMedian'},
                    {'label': '2022 April - September Outer Shell', 'value': '2022ASOuter'},
                    {'label': '2022 June - September Mean', 'value': '2022JSMean'},
                    {'label': '2022 June - September Median', 'value': '2022JSMedian'},
                    {'label': '2022 June - September Outer Shell', 'value': '2022JSOuter'},
                    {'label': 'Synthetic Dry-Wet-Dry Mean', 'value': 'DWDMean'},
                    {'label': 'Synthetic Dry-Wet-Dry Median', 'value': 'DWDMedian'},
                    {'label': 'Synthetic Dry-Wet-Dry Outer Shell', 'value': 'DWDOuter'},
                    {'label': 'Synthetic Wet-Dry-Wet Mean', 'value': 'WDWMean'},
                    {'label': 'Synthetic Wet-Dry-Wet Median', 'value': 'WDWMedian'},
                    {'label': 'Synthetic Wet-Dry-Wet Outer Shell', 'value': 'WDWOuter'}
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
        df = pd.read_feather('data/outputs/2021 Output/output_2021_1_8.ftr')
        title = '2021 Nelson Model June - August vs Precipitation'

    elif value == '2021AD':
        df = pd.read_feather('data/outputs/2021 Output/output_2021_8_12.ftr')
        title = '2021 Nelson Model August - December vs Precipitation'
    
    elif value == '2022ASMean':
        df = pd.read_feather('data/outputs/April-Sept Output/output_mean_AS.ftr')
        title = '2022 Nelson Model Mean April - September vs Precipitation'

    elif value == '2022ASMedian':
        df = pd.read_feather('data/outputs/April-Sept Output/output_median_AS.ftr')
        title = '2022 Nelson Model Median April - September vs Precipitation'

    elif value == '2022ASOuter':
        df = pd.read_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')
        title = '2022 Nelson Model Outer April - September vs Precipitation'

    elif value == '2022JSMean':
        df = pd.read_feather('data/outputs/June-Sept Output/output_mean_JS.ftr')
        title = '2022 Nelson Model Mean June - September vs Precipitation'

    elif value == '2022JSMedian':
        df = pd.read_feather('data/outputs/June-Sept Output/output_median_JS.ftr')
        title = '2022 Nelson Model Median June - September vs Precipitation'
    
    elif value == '2022JSOuter':
        df = pd.read_feather('data/outputs/June-Sept Output/output_outer_JS.ftr')
        title = '2022 Nelson Model Outer June - September vs Precipitation'

    elif value == 'DWDMean':
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_median.ftr')
        title = 'Synthetic Dry-Wet-Dry Mean vs Precipitation'

    elif value == 'DWDMedian':
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_median.ftr')
        title = 'Synthetic Dry-Wet-Dry Median vs Precipitation'

    elif value == 'DWDOuter':
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_outer.ftr')
        title = 'Synthetic Dry-Wet-Dry Outer vs Precipitation'

    elif value == 'WDWMean':
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_mean.ftr')
        title = 'Synthetic Wet-Dry-Wet Mean vs Precipitation'

    elif value == 'WDWMedian':
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_median.ftr')
        title = 'Synthetic Wet-Dry-Wet Median vs Precipitation'

    elif value == 'WDWOuter':
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_outer.ftr')
        title = 'Synthetic Wet-Dry-Wet Outer vs Precipitation'

    else:
        select_graph('2021JA')   

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=df['time'], y=df['precip'], name="Precip (cm)"),
        secondary_y=True
    )
    fig.update_traces(width=5, opacity=0.6)
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
    fig.update_layout(title="<b>"+ title+"</b>")
    return fig      

    # This sets the server ip and port. As well as enables debugging, which is needed to force reload when feather files change
if __name__ == '__main__':
    app.run_server(debug=True)

    #host='0.0.0.0', port = '8050', 