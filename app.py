#import requests
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd

data = pd.read_excel("data/data.xlsx")
BS = "assets/bootstrap.min.css"#"https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[BS])
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
print("OK")
PLOTLY_LOGO = "assets/plotly-logomark.png"#"https://images.plot.ly/logo/new-branding/plotly-logomark.png"
items = [
    dbc.DropdownMenuItem("Item 1"),
    dbc.DropdownMenuItem("Item 2"),
    dbc.DropdownMenuItem("Item 3"),
]

dropdowns = html.Div(
    [
        dbc.DropdownMenu(
            items, label="Primary", color="primary", className="m-1"
        ),
        dbc.DropdownMenu(
            items, label="Secondary", color="secondary", className="m-1"
        ),
        dbc.DropdownMenu(
            items, label="Success", color="success", className="m-1"
        ),
        dbc.DropdownMenu(
            items, label="Warning", color="warning", className="m-1"
        ),
        dbc.DropdownMenu(
            items, label="Danger", color="danger", className="m-1"
        ),
        dbc.DropdownMenu(items, label="Info", color="info", className="m-1"),
        dbc.DropdownMenu(items, label="Link", color="link", className="m-1"),
    ],
    style={"display": "flex", "flexWrap": "wrap"},
)
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ml-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Фильтры", className="ml-2")),
                    #dbc.Col(dbc.DropdownMenu("dropdowns", className="ml-2")),
                ],
                #align="center",
                #no_gutters=True,
            ),
            #href="http://127.0.0.1:8050/",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            dropdowns, id="navbar-collapse", navbar=True, is_open=False
        ),
    ],
    color="dark",
    dark=True,
)
IF
card_content = [
    dbc.CardHeader("Доступность"),
    dbc.CardBody(
        [
            html.H3("Расчетный % доступности",
                        className="card-title"),
            dbc.Col(
            [
                html.H5("Расчетный % отклонения от предыдущего периода",
                className="card-title"),
                #html.Img(PLOTLY_LOGO),
                #<div>Автор иконок: <a href="http://catalinfertu.com" title="Catalin Fertu">Catalin Fertu</a> from <a href="https://www.flaticon.com/ru/" title="Flaticon">www.flaticon.com</a></div>
            ],
            className="mb-4"),
            html.P(
                "Комментарий",
                className="card-text",
            ),
        ],
        className="mb-4",
    ),
]
color = "info"
#if
row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color=color, outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="success", outline=True)),
        dbc.Col(dbc.Card(card_content, color="warning", outline=True)),
        dbc.Col(dbc.Card(card_content, color="danger", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="light", outline=True)),
        dbc.Col(dbc.Card(card_content, color="dark", outline=True)),
    ]
)

app.layout = html.Div(
        children=[
            html.H1(children="Avocado Analytics",className = "display-1"),
            html.P(
             children="Analyze the behavior of avocado prices"
             " and the number of avocados sold in the US"
             " between 2015 and 2018",
            ),
            html.Div(
                [
                    dbc.Col(navbar),
                ],
                className="mb-4",
            ),
            html.Div([row_1])#, row_2, row_3])
     ]
 )

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True, host = '127.0.0.1')
