# -*- coding: utf-8 -*-
'''
Created on Tue Apr 25 10:57:10 2023

@author: Isaac
'''
# Import dash packages. Note dcc is Dash Core Components
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Import pandas for dataframe objects
import pandas as pd

import plotly.express as px

# Import the library for downloading hydrologic data from the National Water Information System (NWIS).
import dataretrieval.nwis as nwis

# specify the U.S. Geological Survey (USGS) site code for which we want data.
siteCode = '02138500' # This is for Linville River Near Nebo, NC.


# get discharge rates from USGS API
# get instantaneous discharge rates (iv) for a couple days as an example.
df = nwis.get_record(sites=siteCode, service='iv', start='2023-4-23', end='2023-4-26')

# dataframe has a datetime index but to plot the index needs to be a column.
df.reset_index(inplace=True)

# dump dataframe info for debugging
df.info()

# Rename columns to something readable 
df = df.rename(columns={'datetime': 'DateTime', '00060': 'FlowRate'}, errors='raise')

# set axis labels
# x='datetime', y='00060', xlabel='DateTime', ylabel='Discharge (ft3/s)'

# compose the graph
fig = px.line(df, x='DateTime', y='FlowRate', title='Linville River Flow Gauge')

# Initialize Dash app
app = Dash(__name__)

#App layout
app.layout = html.Div([
    html.Div(children='Linville River Flow Gauge'),
    dcc.Graph(figure=fig, id='graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10, id='table')
])

# app.layout = dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})

# app.layout = html.Div([
#     html.Div(children='My First App with Data'),
#     dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})
# ])


# Add controls to build the interaction
# @callback(
#     Output(component_id='graph', component_property='figure'),
#     Input(component_id='table', component_property='value')
# )
def update_graph(col_chosen):
    fig = px.line(df, x='DateTime', y='FlowRate', title='Linville River Flow Gauge')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)