import pandas as pd
import plotly.express as px
import dash
from datetime import date
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import time
import re

# Instantiation of the app and supression of startup exceptions
# This is done to account for my multiple app.callbacks on each page
app = dash.Dash(__name__, suppress_callback_exceptions=True)

#This is the first layer of HTML elements
app.layout = html.Div(children=[
    html.H1(children='United States Weather Stations', style={'text-align': 'center'}),

    html.Br(), html.Br(),
            html.Label(['Choose a map:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Temperature', 'value': 'temp'},
                    {'label': 'Dew Point Temperature', 'value': 'dew_point'},
                    {'label': 'Relative Humidity', 'value': 'humid'},
                    {'label': 'Wind Speed', 'value': 'wind_speed'},
                    {'label': 'Wind Gust', 'value': 'wind_gust'},
                    {'label': 'Pressure', 'value': 'pressure'},
                    {'label': 'Precipitation 24hr', 'value': 'precip_24hr'},
                    {'label': 'Fosberg Fire Index', 'value': 'fire_index'},
                    {'label': 'Heat Index', 'value': 'heat_index'},
                    {'label': 'Fuel Temp', 'value': 'fuel_temp'},
                    {'label': 'Fuel Moisture', 'value': 'fuel_moist'}
                        ],
                value='temp',
                style={"width": "60%"}),
            
            html.Div(dcc.Graph(id='map')),
])    
@app.callback(
    Output('map', 'figure'),
    Output('timestamp', 'children'),
    [Input(component_id='dropdown', component_property='value')],
)
def select_graph(value):
    if value == 'temp':
        df_temp = pd.read_feather('./assets/latest.ftr')
        fig_temp = px.scatter_mapbox(df_temp, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Temperature"],
                        color= "Temperature", color_continuous_scale="turbo",
                           range_color=(50, 110), zoom=3, height=300)
        fig_temp.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_temp.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_temp, str(df_temp["Timestamp"][0])


    elif value == 'dew_point':
        df_dew = pd.read_feather('./assets/latest.ftr')
        fig_dew = px.scatter_mapbox(df_dew, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Dew_Point_Temp"],
                        color= "Dew_Point_Temp", color_continuous_scale="turbo",
                           range_color=(50, 110), zoom=3, height=300)
        fig_dew.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_dew.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_dew, str(df_dew["Timestamp"][0])


    elif value == 'humid':
        df_humid = pd.read_feather('./assets/latest.ftr')
        fig_humid = px.scatter_mapbox(df_humid, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Relative_Humidity"],
                        color= "Relative_Humidity", color_continuous_scale="turbo",
                           range_color=(0, 100), zoom=3, height=300)
        fig_humid.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_humid.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_humid, str(df_humid["Timestamp"][0])


    elif value == 'wind_speed':
        df_wind_speed =pd.read_feather('./assets/latest.ftr')
        fig_wind_speed = px.scatter_mapbox(df_wind_speed, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Wind_Speed"],
                        color= "Wind_Speed", color_continuous_scale="turbo",
                           range_color=(0, 20), zoom=3, height=300)
        fig_wind_speed.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_wind_speed.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_wind_speed, str(df_wind_speed["Timestamp"][0])
        

    elif value == 'wind_gust':
        df_wind_gust = pd.read_feather('./assets/latest.ftr')
        fig_wind_gust = px.scatter_mapbox(df_wind_gust, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Wind_Gust"],
                        color= "Wind_Gust", color_continuous_scale="turbo",
                           range_color=(0, 20), zoom=3, height=300)
        fig_wind_gust.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_wind_gust.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_wind_gust, str(df_wind_gust["Timestamp"][0])
        

    elif value == 'pressure':
        df_pressure = pd.read_feather('./assets/latest.ftr')
        fig_pressure = px.scatter_mapbox(df_pressure, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Pressure"],
                        color= "Pressure", color_continuous_scale="turbo",
                           range_color=(800, 1100), zoom=3, height=300)
        fig_pressure.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_pressure.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_pressure, str(df_pressure["Timestamp"][0])
        

    elif value == 'precip_24hr':
        df_precip = pd.read_feather('./assets/latest.ftr')
        fig_precip = px.scatter_mapbox(df_precip, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Precipitation_24hr"],
                        color= "Precipitation_24hr", color_continuous_scale="turbo",
                           range_color=(0, 3), zoom=3, height=300)
        fig_precip.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_precip.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_precip, str(df_precip["Timestamp"][0])
        
    
    elif value == 'fire_index':
        df_fire_index = pd.read_feather('./assets/latest.ftr')
        fig_fire_index = px.scatter_mapbox(df_fire_index, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Fire_Index"],
                        color= "Fire_Index", color_continuous_scale="turbo",
                           range_color=(0, 30), zoom=3, height=300)
        fig_fire_index.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_fire_index.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_fire_index, str(df_fire_index["Timestamp"][0])
        

    elif value == 'heat_index':
        df_heat_index = pd.read_feather('./assets/latest.ftr')
        fig_heat_index = px.scatter_mapbox(df_heat_index, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Heat_Index"],
                        color= "Heat_Index", color_continuous_scale="turbo",
                           range_color=(50, 110), zoom=3, height=300)
        fig_heat_index.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_heat_index.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_heat_index, str(df_heat_index["Timestamp"][0])
        

    elif value == 'fuel_temp':
        df_fuel_temp = pd.read_feather('./assets/latest.ftr')
        fig_fuel_temp = px.scatter_mapbox(df_fuel_temp, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Fuel_Temp"],
                        color= "Fuel_Temp", color_continuous_scale="turbo",
                           range_color=(50, 110), zoom=3, height=300)
        fig_fuel_temp.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_fuel_temp.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_fuel_temp, str(df_fuel_temp["Timestamp"][0])


    elif value == 'fuel_moist':
        df_fuel_moist= pd.read_feather('./assets/latest.ftr')
        fig_fuel_moist = px.scatter_mapbox(df_fuel_moist, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name", "Fuel_Moisture"],
                        color= "Fuel_Moisture", color_continuous_scale="rdylbu",
                           range_color=(0, 30), zoom=3, height=300)
        fig_fuel_moist.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig_fuel_moist.update_layout(
        autosize=False,
        margin = dict(
                l=0,
                r=0,
                b=0,
                t=0,
                pad=4,
                autoexpand=True
            ),
            height=800,
    )
        return fig_fuel_moist, str(df_fuel_moist["Timestamp"][0])

    else:
        select_graph('temp')        

    # This sets the server ip and port. As well as enables debugging, which is needed to force reload when feather files change
if __name__ == '__main__':
    app.run_server(debug=True)

    #host='0.0.0.0', port = '8050', 