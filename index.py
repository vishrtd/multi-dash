from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc


from app import app
from apps import app1, app2

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("App1", href="/app1"),
        dbc.DropdownMenuItem("App2", href="/app2"),
    ],
    nav=True,
    in_navbar=True,
    label="Explore",
)

navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
              dbc.Col(html.Img(src='/assets/logo.png', height='30px')),
              dbc.Col(dbc.NavbarBrand('App1', class_name='ml-2'))
            ], align='center'), href='/home'
        ),
        dbc.NavbarToggler(id='navbar-toggler2'),
        dbc.Collapse(
        dbc.Nav(
            [dropdown], class_name='ml-auto', navbar=True
        ),
        id='navbar-collapse2',
        navbar=True
        ),
    ]), color='light', class_name='mb-4', style={'text_color': 'primary'}
)



def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f'navbar-collapse{i}','is_open'),
        Input(f'navbar-toggler{i}', 'n_clicks'),
        State(f'navbar-collapse{i}', 'is_open')
    )(toggle_navbar_collapse)

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='page-content')
    ])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/app2':
        return app2.layout
    return app1.layout

if __name__ == '__main__':
    app.run_server(debug=True)
