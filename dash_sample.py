import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#Loading Dataset
avacado = pd.read_csv('')


#Creating dash App
app = dash.Dash()



#Setting App Layout

app.layout = html.Div(children=[
    html.H1(),
    dcc.Dropdown()
])



#Setup callback fuction




