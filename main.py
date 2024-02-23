import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('data.csv')

names = df.columns[1:]

@app.callback(
    dash.Output('graph', 'figure'), 
    dash.Input('values', 'value'))
def generate_chart(values):
    fig = px.pie(df, values=df.iloc[values].values[1:], names=names, hole=.3)
    return fig

app.layout = html.Div(children=[
   html.H1(children='Доли продаж компаний-производителей телефонов по кварталам 2018-2020 гг'),

   dcc.Slider(0, 10, 1, marks={i: list(df['Quarter'])[i] for i in range(11)}, value=5, id='values'),

   dcc.Graph(
       id='graph',
   )
])

if __name__ == '__main__':
   app.run_server(debug=True)
