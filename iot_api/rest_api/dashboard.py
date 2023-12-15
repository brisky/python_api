import requests
import datetime

import plotly.express as px
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import settings as sets

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) # external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H2('IoT Temperature Dashboard'),
        html.Br(),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=6*1000,  # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-text', 'children'),
              Input('interval-component', 'n_intervals'))
def update_realtime(n):
    result = requests.get(sets.REALTIME_URL)
    print('Requesting realtime...')
    if result.status_code == 200:
        data = result.json()
        timestamp = [datetime.datetime.strptime(row['timestamp'],
                    "%Y-%m-%d %H:%M:S.%f") for row in data]
        temperature = [row['value'] for row in data]
        # temperature = result.json()["value"]
        return html.Span("Temperature: " + str(temperature))


@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    result = requests.get(sets.HISTORY_URL)
    print('Requesting history...')
    if result.status_code == 200:
        data = result.json()
        timestamp = [datetime.datetime.strptime(row['timestamp'],
                     "%a, %d %b %Y %H:%M:%S GMT") for row in data]
        temperature = [row['value'] for row in data]
        fig = px.line(x=timestamp, y=temperature,
                      labels={'x': 'time', 'y': 'celsius'})
        return fig


def main():
    app.run_server(host="0.0.0.0", port=5080, debug=False)


if __name__ == '__main__':
    print('Staring dashboard...')
    main()