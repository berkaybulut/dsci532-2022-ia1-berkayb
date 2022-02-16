import os
from dash import Dash, dcc, html, Input, Output
import altair as alt
from vega_datasets import data

    
plot_data = data.cars()

def plot_altair(xmax):
    chart = alt.Chart(plot_data[plot_data['Year'] < xmax]).mark_line().encode(
        x='Year',
        y='Deaths')
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            srcDoc=plot_altair(xmax=2017),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=1900, max=2017)])
        
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'))
def update_output(xmax):
    return plot_altair(xmax)

if __name__ == '__main__':
    app.run_server(debug=True)