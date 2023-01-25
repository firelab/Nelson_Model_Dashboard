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
    html.H1(children='Nelson Model Test Results', style={'text-align': 'center'}),

    html.Br(), html.Br(),
            html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': '2021 January - August All', 'value': '2021JA'},
                    {'label': '2021 January - August Mean', 'value': '2021JAMean'},
                    {'label': '2021 January - August Median', 'value': '2021JAMedian'},
                    {'label': '2021 January - August Outer Shell', 'value': '2021JAOuter'},
                    {'label': '2021 August - Decemeber All', 'value': '2021AD'},
                    {'label': '2021 August - Decemeber Mean', 'value': '2021ADMean'},
                    {'label': '2021 August - Decemeber Median', 'value': '2021ADMedian'},
                    {'label': '2021 August - Decemeber Outer Shell', 'value': '2021ADOuter'},
                    {'label': '2022 April - September All', 'value': '2022AS'},
                    {'label': '2022 April - September Mean', 'value': '2022ASMean'},
                    {'label': '2022 April - September Median', 'value': '2022ASMedian'},
                    {'label': '2022 April - September Outer Shell', 'value': '2022ASOuter'},
                    {'label': '2022 June - September All', 'value': '2022JS'},
                    {'label': '2022 June - September Mean', 'value': '2022JSMean'},
                    {'label': '2022 June - September Median', 'value': '2022JSMedian'},
                    {'label': '2022 June - September Outer Shell', 'value': '2022JSOuter'},
                    {'label': 'Synthetic Dry-Wet-Dry All', 'value': 'DWD'},
                    {'label': 'Synthetic Dry-Wet-Dry Mean', 'value': 'DWDMean'},
                    {'label': 'Synthetic Dry-Wet-Dry Median', 'value': 'DWDMedian'},
                    {'label': 'Synthetic Dry-Wet-Dry Outer Shell', 'value': 'DWDOuter'},
                    {'label': 'Synthetic Wet-Dry-Wet All', 'value': 'WDW'},
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
        check = True
        df = pd.read_feather('data/outputs/2021 Output/2021_1_8_Mean.ftr')
        df2 = pd.read_feather('data/outputs/2021 Output/2021_1_8_Median.ftr')
        df3 = pd.read_feather('data/outputs/2021 Output/2021_1_8_Outer.ftr')
        title = '2021 Nelson Model All January - August vs Precipitation'

    elif value == '2021JAMean':
        check = False
        df = pd.read_feather('data/outputs/2021 Output/2021_1_8_Mean.ftr')
        title = '2021 Nelson Model Mean January - August vs Precipitation'

    elif value == '2021JAMedian':
        check = False
        df = pd.read_feather('data/outputs/2021 Output/2021_1_8_Median.ftr')
        title = '2021 Nelson Model Median January - August vs Precipitation'

    elif value == '2021JAOuter':
        check = False
        df = pd.read_feather('data/outputs/2021 Output/2021_1_8_Outer.ftr')
        title = '2021 Nelson Model Outer January - August vs Precipitation'

    elif value == '2021AD':
        check = True
        df = pd.read_feather('data/outputs/2021 Output/2021_8_12_Mean.ftr')
        df2 = pd.read_feather('data/outputs/2021 Output/2021_8_12_Median.ftr')
        df3 = pd.read_feather('data/outputs/2021 Output/2021_8_12_Outer.ftr')
        title = '2021 Nelson Model All August - December vs Precipitation'

    elif value == '2021ADMean':
        check = False
        df = pd.read_feather('data/outputs/2021 Output/2021_8_12_Mean.ftr')
        title = '2021 Nelson Model Mean August - December vs Precipitation'

    elif value == '2021ADMedian':
        check = False
        df = pd.read_feather('data/outputs/2021 Output/2021_8_12_Median.ftr')
        title = '2021 Nelson Model Median August - December vs Precipitation'

    elif value == '2021ADOuter':
        check = False
        df = pd.read_feather('data/outputs/2021 Output/2021_8_12_Outer.ftr')
        title = '2021 Nelson Model Outer August - December vs Precipitation'
    
    elif value == '2022AS':
        check = True
        df = pd.read_feather('data/outputs/April-Sept Output/output_mean_AS.ftr')
        df2 = pd.read_feather('data/outputs/April-Sept Output/output_median_AS.ftr')
        df3 = pd.read_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')
        title = '2022 Nelson Model All April - September vs Precipitation'
    
    elif value == '2022ASMean':
        check = False
        df = pd.read_feather('data/outputs/April-Sept Output/output_mean_AS.ftr')
        title = '2022 Nelson Model Mean April - September vs Precipitation'

    elif value == '2022ASMedian':
        check = False
        df = pd.read_feather('data/outputs/April-Sept Output/output_median_AS.ftr')
        title = '2022 Nelson Model Median April - September vs Precipitation'

    elif value == '2022ASOuter':
        check = False
        df = pd.read_feather('data/outputs/April-Sept Output/output_outer_AS.ftr')
        title = '2022 Nelson Model Outer April - September vs Precipitation'

    elif value == '2022JS':
        check = True
        df = pd.read_feather('data/outputs/June-Sept Output/output_mean_JS.ftr')
        df2 = pd.read_feather('data/outputs/June-Sept Output/output_median_JS.ftr')
        df3 = pd.read_feather('data/outputs/June-Sept Output/output_outer_JS.ftr')
        title = '2022 Nelson Model All June - September vs Precipitation'

    elif value == '2022JSMean':
        check = False
        df = pd.read_feather('data/outputs/June-Sept Output/output_mean_JS.ftr')
        title = '2022 Nelson Model Mean June - September vs Precipitation'

    elif value == '2022JSMedian':
        check = False
        df = pd.read_feather('data/outputs/June-Sept Output/output_median_JS.ftr')
        title = '2022 Nelson Model Median June - September vs Precipitation'
    
    elif value == '2022JSOuter':
        check = False
        df = pd.read_feather('data/outputs/June-Sept Output/output_outer_JS.ftr')
        title = '2022 Nelson Model Outer June - September vs Precipitation'

    elif value == 'DWD':
        check = True
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_mean.ftr')
        df2 = pd.read_feather('data/outputs/DWD output/output_syn_dwd_median.ftr')
        df3 = pd.read_feather('data/outputs/DWD output/output_syn_dwd_outer.ftr')
        title = 'Synthetic Dry-Wet-Dry All vs Precipitation'

    elif value == 'DWDMean':
        check = False
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_mean.ftr')
        title = 'Synthetic Dry-Wet-Dry Mean vs Precipitation'

    elif value == 'DWDMedian':
        check = False
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_median.ftr')
        title = 'Synthetic Dry-Wet-Dry Median vs Precipitation'

    elif value == 'DWDOuter':
        check = False
        df = pd.read_feather('data/outputs/DWD output/output_syn_dwd_outer.ftr')
        title = 'Synthetic Dry-Wet-Dry Outer vs Precipitation'

    elif value == 'WDW':
        check = True
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_mean.ftr')
        df2 = pd.read_feather('data/outputs/WDW output/output_syn_wdw_median.ftr')
        df3 = pd.read_feather('data/outputs/WDW output/output_syn_wdw_outer.ftr')
        title = 'Synthetic Wet-Dry-Wet All vs Precipitation'

    elif value == 'WDWMean':
        check = False
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_mean.ftr')
        title = 'Synthetic Wet-Dry-Wet Mean vs Precipitation'

    elif value == 'WDWMedian':
        check = False
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_median.ftr')
        title = 'Synthetic Wet-Dry-Wet Median vs Precipitation'

    elif value == 'WDWOuter':
        check = False
        df = pd.read_feather('data/outputs/WDW output/output_syn_wdw_outer.ftr')
        title = 'Synthetic Wet-Dry-Wet Outer vs Precipitation'

    else:
        select_graph('2021JA')   
    if not check:
    # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Bar(x=df['time'], y=df['precip'], name="Precip (cm)"),
            secondary_y=True
        )
        fig.update_traces(width=5, opacity=0.5)
        fig.add_trace(
            go.Scatter(x=df['time'], y=df['1hrfm'], name="1hrfm", opacity= .6),
            secondary_y=False
        )
        fig.add_trace(
            go.Scatter(x=df['time'], y=df['10hrfm'], name="10hrfm", opacity= .6),
            secondary_y=False
        )
        fig.add_trace(
            go.Scatter(x=df['time'], y=df['100hrfm'], name="100hrfm", opacity= .6),
            secondary_y=False
        )
        fig.add_trace(
            go.Scatter(x=df['time'], y=df['1000hrfm'], name="1000hrfm", opacity= .6),
            secondary_y=False
        )

        fig.update_yaxes(title_text="<b>Nelson Model</b>", secondary_y=False)
        fig.update_yaxes(title_text="<b>Precip (cm)</b>", secondary_y=True)
        fig.update_xaxes(title_text="<b>Date and Time</b>")
        fig.update_layout(title="<b>"+ title+"</b>")
    else:
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

if __name__ == '__main__':
    app.run_server(debug=True)

    #host='0.0.0.0', port = '8050', 