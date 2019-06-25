# -*- coding: utf-8 -*-

import pprint
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import  plotly.plotly as py
import  plotly.tools as tls


cat = 0

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


def criar_grafico_bar2(uf, df):
    trace = []
    uf = list(uf)
    for i in range(len(uf)):
        trace.append(
            go.Bar(
                x=[uf[i]],
                y=[len(df[df['uf'] == uf[i]])],
                name=(uf[i])
            ),
        )


    return [
        dcc.Graph(
            id='example-graph',
            figure={
                'data': trace,
                'layout': {
                    'title': 'Numeros de acidentes por Estado do ano de 2007 a 2018'
                }
            }
        )
    ]


def criar_grafico_bar3(ano, uf, df):
    trace = []

    for i in range(len(uf)):
        trace.append(
            go.Bar(
                x=[(uf[i])],
                y=[len(df[(df['uf'] == uf[i]) & (df['ano'] == ano)])],
                name=(uf[i])),
        )

    return [
        dcc.Graph(
            id='example-graph',
            figure={
                'data': trace,
                'layout': {
                    'title': 'Numeros de acidentes por Estado no ano de {}'.format(ano)
                }
            }
        )
    ]

def criar_grafico_bar4(ano, df, uf):
    trace = []
    d = df.dia_semana.unique()
    d = list(d)
    if uf != 'sim':
        for i in range(len(d)):
            trace.append(
                go.Bar(
                    x=[(d[i])],
                    y=[len(df[(df['dia_semana'] == d[i]) & (df['ano'] == ano)])],
                    name=(d[i])),
            )
    else:
        for i in range(len(d)):
            trace.append(
                go.Bar(
                    x=[(d[i])],
                    y=[len(df[(df['dia_semana'] == d[i])])],
                    name=(d[i])),
            )
        ano = [2007, 2018]

    return [
        dcc.Graph(
            id='example-graph',
            figure={
                'data': trace,
                'layout': {
                    'title': 'Numeros de acidentes por dia da semana no ano de {}'.format(ano)
                }
            }
        )
    ]


df = pd.read_csv('csv/datatranAll.csv', low_memory=False)



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('SELECIONE A CATEGORIA'),
    dcc.Dropdown(
        id='categorias',
        options=[
            {'label': 'Acidentes total por ano', 'value': 'qnt_a'},
            {'label': 'Acidentes total por estado', 'value': 'uf'},
            {'label': 'Acidentes por dia da semana no ano', 'value': 'dia'},
            {'label': 'Acidentes por ano e estado', 'value': 'qnt_a_uf'}


        ],
        value='qnt_a'
    ),
    html.Div(id='minha-saida'),

    html.Hr(),


    html.Div(id='minha-saida2'),

])





@app.callback(Output('minha-saida', 'children'),
              [Input(component_id='categorias', component_property='value')])
def update_output(categoria):
    global cat
    if categoria == 'qnt_a':
        cat = 1
        return (
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
                    value=[2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
                    multi=True

                ),
            dcc.Upload(id='sel_uf')
         )

    elif categoria == 'uf':
        cat = 0
        return (
                dcc.Upload(id='ano'),
                html.Label('SELECIONE O(S) ESTADO(S)'),
                dcc.Dropdown(
                    id='sel_uf',
                    options=[{'label': 'MG', 'value': 'MG'},
                             {'label': 'MA', 'value': 'MA'},
                             {'label': 'CE', 'value': 'CE'},
                             {'label': 'PR', 'value': 'PR'},
                             {'label': 'ES', 'value': 'ES'},
                             {'label': 'GO', 'value': 'GO'},
                             {'label': 'RJ', 'value': 'RJ'},
                             {'label': 'RS', 'value': 'RS'},
                             {'label': 'SP', 'value': 'SP'},
                             {'label': 'RN', 'value': 'RN'},
                             {'label': 'SC', 'value': 'SC'},
                             {'label': 'PA', 'value': 'PA'},
                             {'label': 'PE', 'value': 'PE'},
                             {'label': 'MT', 'value': 'MT'},
                             {'label': 'BA', 'value': 'BA'},
                             {'label': 'AL', 'value': 'AL'},
                             {'label': 'TO', 'value': 'TO'},
                             {'label': 'PI', 'value': 'PI'},
                             {'label': 'MS', 'value': 'MS'},
                             {'label': 'SE', 'value': 'SE'},
                             {'label': 'RO', 'value': 'RO'},
                             {'label': 'PB', 'value': 'PB'},
                             {'label': 'AP', 'value': 'AP'},
                             {'label': 'DF', 'value': 'DF'},
                             {'label': 'AC', 'value': 'AC'},
                             {'label': 'RR', 'value': 'RR'},
                             {'label': 'AM', 'value': 'AM'}],
                    value=['MG', 'MA', 'CE', 'PR', 'ES', 'GO', 'RJ', 'RS', 'SP', 'RN', 'SC', 'PA', 'PE', 'MT', 'BA',
                           'AL', 'TO',
                           'PI', 'MS', 'SE', 'RO', 'PB', 'AP', 'DF', 'AC', 'RR', 'AM'],
                    multi=True

                )
        )

    elif categoria =='qnt_a_uf':
        cat = 2
        return (
               html.Label('SELECIONE O ANO'),
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
                   value=2007

               ),

                html.Label('SELECIONE O(S) ESTADO(S)'),
                dcc.Dropdown(
                    id='sel_uf',
                    options=[{'label': 'MG', 'value': 'MG'},
                             {'label': 'MA', 'value': 'MA'},
                             {'label': 'CE', 'value': 'CE'},
                             {'label': 'PR', 'value': 'PR'},
                             {'label': 'ES', 'value': 'ES'},
                             {'label': 'GO', 'value': 'GO'},
                             {'label': 'RJ', 'value': 'RJ'},
                             {'label': 'RS', 'value': 'RS'},
                             {'label': 'SP', 'value': 'SP'},
                             {'label': 'RN', 'value': 'RN'},
                             {'label': 'SC', 'value': 'SC'},
                             {'label': 'PA', 'value': 'PA'},
                             {'label': 'PE', 'value': 'PE'},
                             {'label': 'MT', 'value': 'MT'},
                             {'label': 'BA', 'value': 'BA'},
                             {'label': 'AL', 'value': 'AL'},
                             {'label': 'TO', 'value': 'TO'},
                             {'label': 'PI', 'value': 'PI'},
                             {'label': 'MS', 'value': 'MS'},
                             {'label': 'SE', 'value': 'SE'},
                             {'label': 'RO', 'value': 'RO'},
                             {'label': 'PB', 'value': 'PB'},
                             {'label': 'AP', 'value': 'AP'},
                             {'label': 'DF', 'value': 'DF'},
                             {'label': 'AC', 'value': 'AC'},
                             {'label': 'RR', 'value': 'RR'},
                             {'label': 'AM', 'value': 'AM'}],
                    value=['MG', 'MA', 'CE', 'PR', 'ES', 'GO', 'RJ', 'RS', 'SP', 'RN', 'SC', 'PA', 'PE', 'MT', 'BA', 'AL', 'TO',
                           'PI', 'MS', 'SE', 'RO', 'PB', 'AP', 'DF', 'AC', 'RR', 'AM'],
                    multi=True

                )
        )
    elif categoria == 'dia':
        cat = 3
        return (
            html.Label('SELECIONE O ANO'),
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
                value=2007

            ),
            html.Label('TODOS OS ANOS ?'),
            dcc.RadioItems(
                id='sel_uf',
                options=[{'label': i, 'value': i} for i in ['sim', 'não']],
                value='sim',
                labelStyle={'display': 'inline-block'}
            )
        )



app.config['suppress_callback_exceptions'] = True

@app.callback(Output('minha-saida2', 'children'),
              [Input(component_id='ano', component_property='value'),
               Input(component_id='sel_uf', component_property='value')])
def gerar_grafico(ano, uf):

    if cat == 1:
        return criar_grafico_bar(ano, df)

    elif cat == 0:
        return criar_grafico_bar2(uf, df)

    elif cat == 2:
        return criar_grafico_bar3(ano, uf, df)

    elif cat == 3:
        return criar_grafico_bar4(ano, df, uf)


if __name__ == '__main__':
    app.run_server(debug=True)