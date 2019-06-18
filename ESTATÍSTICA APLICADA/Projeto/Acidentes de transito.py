import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('csv/datatranAll.csv', low_memory=False)




trace1 = go.Bar(
    x=['ano 2007'],
    y=[len(df[df['ano']==2007])],
    name='2007'
)

trace2 = go.Bar(
    x=['ano 2008'],
    y=[len(df[df['ano']==2008])],
    name='2008'
)

trace3 = go.Bar(
    x=['ano 2009'],
    y=[len(df[df['ano']==2009])],
    name='2009'
)

trace4 = go.Bar(
    x=['ano 2010'],
    y=[len(df[df['ano']==2010])],
    name='2010'
)


data = [trace1, trace2, trace3, trace4]
layout = go.Layout(barmode='group')

fig = go.Figure(data=data, layout=layout)




app.layout = html.Div(children=[

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)