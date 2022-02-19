from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


plot_data = data.disasters()

def plot_altair(xmax):
    chart = alt.Chart(plot_data[plot_data['Year'].between(1910, xmax)],
                      title=f"Number of Disasters between 1910 to {xmax}").mark_line().encode(
        x=alt.X('Year'),
        y='Deaths')
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
        html.Iframe(
            id='line',
            srcDoc=plot_altair(xmax=2017),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', value=2015, min=1910, max=2017)
        ])
        
@app.callback(
    Output('line', 'srcDoc'),
    Input('xslider', 'value')
    )
def update_output(value):
    return plot_altair(value)

if __name__ == '__main__':
    app.run_server(debug=True)
