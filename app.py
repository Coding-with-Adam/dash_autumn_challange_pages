from dash import Dash, html, dcc, callback, Input, Output, State
import dash
import pandas as pd
import dash_mantine_components as dmc
from data_etl import df_raw
from utils import create_metric_chooser, create_top_n_filter, create_city_filter, create_category_filter, \
    create_vendor_filter, create_bottly_volume_filter, create_simple_grid
import dash_mantine_components as dmc

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Dash Autumn Challange', style={'textAlign': 'center'}),

    html.Div(
        [
            dmc.Button("Filters", id="modal-demo-button"),
            dmc.Modal(
                size='lg',
                title="Dataset Filters",
                id="modal",
                children=create_simple_grid(
                    component_list=[

                        create_metric_chooser(),

                        create_top_n_filter(),

                        create_city_filter(),

                        create_category_filter(),

                        create_vendor_filter(),

                        create_bottly_volume_filter()

                    ]),
            ),
        ]
    ),

    html.Br(),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container
])


@callback(
    Output("modal", "opened"),
    Input("modal-demo-button", "n_clicks"),
    State("modal", "opened"),
    prevent_initial_call=True,
)
def modal_demo(nc1, opened):
    return not opened


if __name__ == '__main__':
    app.run_server(debug=True)
