# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


def criar_grafico_bar(ano, df):
    trace = []

    if list != type(ano):
        trace.append(go.Bar(x=[ano], y=[len(df[df['ano'] == ano])], name=ano))
    else:
        for i in range(len(ano)):
            trace.append(
                go.Bar(
                    x=[(ano[i])],
                    y=[len(df[df['ano'] == ano[i]])],
                    name=(ano[i])),
            )

    return [
        dcc.Graph(
            id='example-graph',
            figure={
                'data': trace,
                'layout': {
                    'title': 'Numeros de acidentes por ano'
                }
            }
        )
    ]


df = pd.read_csv('csv/datatranAll.csv', low_memory=False)



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Selecione Categoria'),
    dcc.Dropdown(
        id='categorias',
        options=[
            {'label': 'Quantidade de acidentes', 'value': 'qnt_a'},
            {'label': 'Estado', 'value': 'uf'}


        ],
        value='uf'
    ),

    html.Label('SELECIONE O(S) ANO(S)'),
    dcc.Dropdown(
        id='ano',
        options=[
            {'label': '2007', 'value': 2007},
            {'label': '2008', 'value': 2008},
            {'label': '2009', 'value': 2009},
            {'label': '2010', 'value': 2010},
            {'label': '2011', 'value': 2011},
            {'label': '2012', 'value': 2012},
            {'label': '2013', 'value': 2013},
            {'label': '2014', 'value': 2014},
            {'label': '2015', 'value': 2015},
            {'label': '2016', 'value': 2016},
            {'label': '2017', 'value': 2017},
            {'label': '2018', 'value': 2018}
        ],
        value='2014',
        multi=True

    ),
    html.Div(id='minha-saida')

])


@app.callback(Output('minha-saida', 'children'),
              [Input(component_id='categorias', component_property='value'),
               Input(component_id='ano', component_property='value')])
def update_output(categoria, ano):
    if categoria == 'qnt_a':
       return criar_grafico_bar(ano, df)


if __name__ == '__main__':
    app.run_server(debug=True)