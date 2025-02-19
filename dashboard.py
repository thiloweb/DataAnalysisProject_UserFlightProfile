import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image
from dataProcessing import data
import math

# Getting main data for cards
total_flights = [tup_val[0] for tup_val in list(data[2].values())[0]][0]
total_distance = [tup_val[1] for tup_val in list(data[2].values())[0]][0]
total_timeMin = [tup_val[2] for tup_val in list(data[2].values())[0]][0]

def time_convert(totmin):
    hrs, min = math.floor(totmin/60), totmin%60
    return f"{hrs}:{min} hrs"

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP,'assets/flightstats_styles.css']
    )
app.layout = dbc.Container(
    [
        dbc.Row([
            html.Img(src=Image.open("assets/airplane.png"), id="airplaneIcon"),
            ], id="iconRow"
        ),
        dbc.Row(
            [        
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                [     
                                    html.Div('DATA ANALYSIS PROJECT "USER FLIGHT PROFILE"', id="header"),
                                    html.Div("Selected data for Europe & the Americas"),
                                ], className="cardContainer projectTitle"
                            ), 
                        ]),
                    ]),                      
                ]),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                [
                                html.Div("Data:"),
                                html.Div(f"{total_flights} flights",),
                                ], className="cardContainer"
                            ),    
                        ]),
                        dbc.Col([
                            html.Div(
                                [
                                    html.Div("Total flight distance:"),
                                    html.Div(f" {total_distance:,} km",),
                                ], className="cardContainer"
                            ),  
                        ]),
                        dbc.Col([
                            html.Div(
                                [
                                    html.Div(f"Total flight time:"),
                                    html.Div(f"{time_convert(total_timeMin)}",),
                                ], className="cardContainer"
                            )  
                        ]),
                    ]),   
                ]),

            ], id="titleRow",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src=Image.open('plots/ratio_flightdistance_pie.png'), className="PlotIMG"),
                ), 
                dbc.Col(
                    html.Img(src=Image.open('plots/flighttime_regional_bar.png'), className="PlotIMG"),
                ),
                dbc.Col(
                    html.Img(src=Image.open('plots/ratio_flights_distance_time_bar.png'), className="PlotIMG"),
                ),
                dbc.Col(
                    html.Img(src=Image.open('plots/ratio_flighttypes_pie.png'), className="PlotIMG"),
                ),
                dbc.Col(
                    html.Img(src=Image.open('plots/top5_airlines_bar.png'), className="PlotIMG"),
                ),
                dbc.Col(
                    html.Img(src=Image.open('plots/top10_airport_countries_bar.png'), className="PlotIMG"),
                ),
            ], id="chartRow"
        ), 
    ], 
    fluid=True
)

if __name__ == "__main__":
    app.run_server(debug=True)