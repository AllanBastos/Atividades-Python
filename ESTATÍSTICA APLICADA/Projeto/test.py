# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Selecione Categoria'),
    dcc.Dropdown(
        options=[
            {'label': 'Quantidade de acidentes', 'value': '2007'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': u'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('SELECIONE O(S) ANO(S)'),
    dcc.Dropdown(
        options=[
            {'label': '2008', 'value': '2008'},
            {'label': '2009', 'value': '2009'},
            {'label': '2010', 'value': '2010'},
            {'label': '2011', 'value': '2011'},
            {'label': '2012', 'value': '2012'},
            {'label': '2013', 'value': '2013'},
            {'label': '2014', 'value': '2014'},
            {'label': '2015', 'value': '2015'},
            {'label': '2016', 'value': '2016'},
            {'label': '2017', 'value': '2017'},
            {'label': '2018', 'value': '2018'}
        ],
        value='MTL',
        multi=True

    ),


], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)