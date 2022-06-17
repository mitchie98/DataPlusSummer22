from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# data
df = pd.read_csv(r'C:\Users\hessi\PycharmProjects\App\processed_UHC_data.csv')

# Page Layout
# ___________________________________________________________________________________________

# App declaration
app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


# Page Layout


app.layout = dbc.Container(
    html.Div(children=[
dbc.Navbar(id='navBar',
        className='w-100',
        children=
    [
        dbc.NavItem(dbc.NavLink("Map", active=True, href="#")),
        dbc.NavItem(dbc.NavLink("Compare", href="#")),
        dbc.NavItem(dbc.NavLink("Browse", href="#")),
        dbc.NavItem(dbc.NavLink("About", href="#")),
    ]
),
    html.Div(id='header', children=[
        html.Title(id='title', children='Map')
    ]),

    html.Div(id='body', children=[
        html.P(id='infoText', children='This will be informational text about the app'),
        dcc.Dropdown(['National Policy',
                       'Prepayment Mechanisms',
                       'Fund Distribution Btwn Schemes',
                       'Fragmentation Prevention',
                       'Linked Payments',
                       'Purchaser-Provider Separation',
                       'Specific Benefits Package',
                       'Point of Car Exemptions'],
                     'National Policy', id='mapDropdown')
    ]),

    dcc.Graph(
        id='graph'
    )])
)


@app.callback(
    Output("graph", "figure"),
    Input("mapDropdown", "value"))
# map
def display_map(mapDropdown):
    map_df = df
    fig = px.choropleth(map_df, locations='Code',
                        color=mapDropdown,
                        hover_name='Name')
    fig.update_layout(
        title_text='Worldwide UHC Policy',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            showocean=True, oceancolor="LightGray",
            projection_type='equirectangular'
            #margin=dict(t=0, b=0, l=0, r=0)
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='',
            showarrow=False
        )],
        legend=dict(
            orientation='h',
            yanchor='top'
        )
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)