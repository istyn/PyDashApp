# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:57:10 2023

@author: Isaac
"""
# Import packages
from dash import Dash, html, dash_table
import pandas as pd
import plotly.express as px

# first import the functions for downloading data from NWIS
import dataretrieval.nwis as nwis

# specify the USGS site code for which we want data.
site = '02138500'


# get discharge rates from USGS API
# get instanteous discharge rates (iv) for a couple days as an example.
df = nwis.get_record(sites=site, service='iv', start='2023-4-23', end='2023-4-25')

# dataframe has a datetime index but to plot the index needs to be a column.
df.reset_index(inplace=True)

# dump dataframe info for debugging
df.info()

# set axis labels
# x="datetime", y="00060", xlabel="DateTime", ylabel="Discharge (ft3/s)"


# compose the graph
fig = px.line(df, x="datetime", y="00060", title='Linville River Flow Gauge').show()

# Initialize the app
app = Dash(__name__)

#App layout
app.layout = html.Div([
    html.Div(children='Linville River Flow Gauge'),
    html.Div(children=fig),
    dash_table.DataTable(data=df.to_dict('records'), page_size=100)
])

# app.layout = dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})

# app.layout = html.Div([
#     html.Div(children='My First App with Data'),
#     dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})
# ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)