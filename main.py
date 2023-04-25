# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:57:10 2023

@author: Isaac
"""

from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.run_server(debug=True)