import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('FPD-non-redundant-processed.csv')
app = dash.Dash()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

#This is the part where you create the graph



#-----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# This is the part where body goes in

app.layout = html.Div([
        html.Div([html.H2('FPD : A Database of Fluorescent Proteins',
                style={
                    'position': 'relative',
                    'top': '0px',
                    'left': '10px',
                    'font-family': 'Dosis',
                    'display': 'inline',
                    'font-size': '6.0rem',
                    'color': '#4D637F'
                }),
                ]),
        html.Div([
                html.P('Center of Data Mining and Biomedical Informatics, Faculty of Medical Technology, Mahidol University'),
            ], style={'margin-left': '10px','font-size' : '1.5rem'}),
        dcc.Slider(
                min=,
                max=9,
                marks={i: 'Label {}'.format(i) for i in range(10)},
                value=5,)
        ])

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "//fonts.googleapis.com/css?family=Dosis:Medium",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/0e463810ed36927caf20372b6411690692f94819/dash-drug-discovery-demo-stylesheet.css"]


for css in external_css:
    app.css.append_css({"external_url": css})
    
if __name__ == '__main__':
    app.run_server(debug=True)
