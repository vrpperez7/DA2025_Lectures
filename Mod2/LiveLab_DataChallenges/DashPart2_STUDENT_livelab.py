import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and clean data
<<<<<<< HEAD
df = pd.read_csv("/Users/beans/Desktop/Marcy_Lab/DA2025_Lectures/Mod2/data/indian_food.csv").dropna()
=======
df = pd.read_csv("None").dropna()
>>>>>>> upstream/main

# Create app
app = dash.Dash(__name__)
app.title = "None"

app.layout = html.Div([
    html.H1("Indian Food Visual Storytelling"),
    dcc.Dropdown(
        id='region-filter',
<<<<<<< HEAD
        options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())],
        placeholder="Select a region",
=======
        options=[{'label': r, 'value': r} for r in sorted(None)],
        placeholder="None",
>>>>>>> upstream/main
        style={'width': '50%'}
    ),
    dcc.Graph(id='flavor-pie')
])

@app.callback(
<<<<<<< HEAD
    Output('flavor-pie', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(region):
    filtered = df[df['region'] == region] if region else df
=======
    Output('None', 'None'),
    Input('None', 'None')
)
def update_chart(region):
    filtered = df[None if region else df
>>>>>>> upstream/main
    fig = px.pie(filtered, names="flavor_profile", title="Flavor Profile Distribution")
    return fig

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> upstream/main
