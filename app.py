from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


plot_data = data.disasters()

def plot_altair(xmin,xmax):
    chart = alt.Chart(plot_data[plot_data['Year'].between(xmin,xmax)]).mark_line().encode(
        x=alt.X('Year'),
        y='Deaths')
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
        html.Iframe(
            id='line',
            srcDoc=plot_altair(xmin=1901, xmax=2017),
            style={'border-width': '0', 'width': '100%', 'height': '400px'})
        ])
        
@app.callback(
    Output('line', 'srcDoc'),
    )
def update_output(xmin,xmax):
    return plot_altair(xmin,xmax)

if __name__ == '__main__':
    app.run_server(debug=True)