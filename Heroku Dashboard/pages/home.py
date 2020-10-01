import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output,Input,State
from dash import no_update
from flask_login import login_user, current_user
import time
from pages import (
    profile,
    )

from server import app

home_login_alert = dbc.Alert(
    'User not logged in. Taking you to login.',
    color='danger'
)

def layout():
    return dbc.Row(
        dbc.Col(
            [
                dcc.Location(id='home-url',refresh=True),
                html.Div(id='home-login-trigger',style=dict(display='none')),

                html.H1('Welcome'),
                html.H1(dbc.Label(id='user-name')),
                html.Br(),

            ],
            width=6
        )
    )

@app.callback(
    Output('home-test','children'),
    [Input('home-test-trigger','children')]
)
def home_test_update(trigger):
    '''
    updates arbitrary value on home page for test
    '''    
    time.sleep(2)
    return html.Div('after the update',style=dict(color='red'))



