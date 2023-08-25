from dash import Dash

from .layout import layout


def viz():
    app = Dash(__name__)
    app.layout = layout()
    return app
