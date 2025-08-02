import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

# Initialize app
app = dash.Dash(__name__)
app.title = "World Trends Dashboard"

# App layout
app.layout = html.Div(id="main-container", children=[
    html.Div([
        html.H1("🌍 World Trends Dashboard", id="header"),
        html.Div([
            html.Label("Select Countries:"),
            dcc.Dropdown(
                id="country-dropdown",
                options=[{"label": c, "value": c} for c in sorted(df["country"].unique())],
                value=["United States", "Canada"],
                multi=True
            ),
        ], style={"width": "40%", "display": "inline-block", "marginRight": "5%"}),

        html.Div([
            html.Label("Select Year Range:"),
            dcc.RangeSlider(
                id="year-slider",
                min=df["year"].min(),
                max=df["year"].max(),
                value=[1970, 2007],
                step=5,
                marks={str(year): str(year) for year in sorted(df["year"].unique())},
                tooltip={"placement": "bottom", "always_visible": False}
            )
        ], style={"width": "50%", "display": "inline-block"})
    ]),

    html.Br(),

    html.Div([
        html.Label("Dark Mode:"),
        dcc.Checklist(
            id="theme-toggle",
            options=[{"label": " Enable Dark Mode", "value": "dark"}],
            value=[],
            style={"marginLeft": "10px"}
        )
    ], style={"textAlign": "center"}),

    html.Br(),

    dcc.Tabs(id="tabs", value="lifeexp", children=[
        dcc.Tab(label="Life Expectancy", value="lifeexp"),
        dcc.Tab(label="GDP per Capita", value="gdp"),
        dcc.Tab(label="Population", value="pop"),
    ]),

    html.Div([
        dcc.Graph(id="main-graph", config={"displaylogo": False}),
    ])
])


@app.callback(
    Output("main-graph", "figure"),
    Input("country-dropdown", "value"),
    Input("year-slider", "value"),
    Input("tabs", "value"),
    Input("theme-toggle", "value")
)
def update_figure(selected_countries, year_range, tab, theme_mode):
    dff = df[df["country"].isin(selected_countries)]
    dff = dff[(dff["year"] >= year_range[0]) & (dff["year"] <= year_range[1])]
    template = "plotly_dark" if "dark" in theme_mode else "plotly_white"

    if tab == "lifeexp":
        fig = px.line(dff, x="year", y="lifeExp", color="country",
                      title="Life Expectancy Over Time", markers=True, template=template)
    elif tab == "gdp":
        fig = px.line(dff, x="year", y="gdpPercap", color="country",
                      title="GDP per Capita Over Time", markers=True, template=template)
    else:
        fig = px.line(dff, x="year", y="pop", color="country",
                      title="Population Over Time", markers=True, template=template)

    fig.update_layout(transition_duration=500)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
