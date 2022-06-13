from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


# data
df = pd.read_csv(r'UHC_Policies_1.csv')
# make the data input into a git link. Maybe make automatic update. Still need to make UTF-8 encoded out of MonQcle

# removing unnecessary columns (caution checks, etc.)
for col in df.columns:
    if col[0:1] == '_':
        df.drop(col, axis=1, inplace=True)

# refactors 1/0 to T/F, for readability in graphics
df = df.replace(1, True)
df = df.replace(0, False)
df = df.fillna('No Data')
# adds code column, necessary to generate map, must figure out how to automate on new data input.
Code = ['GHA', 'KEN', 'ZWE']
df['Code'] = Code

# counts number of policies implemented from the 9 main policies defined in the codebook


def pol_implemented(row):
    c = 0
    if row['national_policy_threshold ']:
        c = c + 1
    if row['prepaid_services']:
        c = c + 1
    if row['redistribution_pooling']:
        c = c + 1
    if row['fragmentation_pooling']:
        c = c + 1
    if row['payments_linked']:
        c = c + 1
    if row['purchasing_separate']:
        c = c + 1
    if row['specifying_benefits']:
        c = c + 1
    if row['specifying_benefits']:
        c = c + 1
    if row['pointofcare_exemptions']:
        c = c + 1
    return c


df['policies_implemented'] = df.apply(lambda row: pol_implemented(row), axis=1)

# proportion of 9 core policies implemented
df['policy_prop'] = df['policies_implemented']/9


# categorizes the proportions into 1 of 5 bins, I think this will go on the map
def bin_prob(row):
    if row['policy_prop'] <= .2:
        return 1
    if .2 < row['policy_prop'] <= .4:
        return 2
    if .4 < row['policy_prop'] <= .6:
        return 3
    if .6 < row['policy_prop'] <= .8:
        return 4
    else:
        return 5


df['prop_binned'] = df.apply(lambda row: bin_prob(row), axis=1)

# Page Layout
# ___________________________________________________________________________________________

# App declaration
app = Dash(__name__)

# figure, need to make into callback function to display multiple policies


app.layout = html.Div(children=[
    html.Title(children='Map'),
    html.H1(children='Map'),

    html.Div(
        dcc.Dropdown(['completed', 'national_policy_threshold ', 'prepaid_services', 'disadvantagedgroups_exemptions'],
                     'completed', id='mapDropdown')
    ),

    dcc.Graph(
        id='graph'
    )
])


@app.callback(
    Output("graph", "figure"),
    Input("mapDropdown", "value"))


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
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='',
            showarrow=False
        )]
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
