import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import pathlib

# Формула расчета:
# Простои = (ОБСЛУЖИВАНИЕ УС + ОТМ + FLM + SLM + Средства + АДМ + ИТ)
# ФРВ – общий фонд работы устройства.
# Доступность сети = Простои/ФРВ в процентах
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

data = pd.read_excel(DATA_PATH.joinpath("data.xlsx"))
# Создадим списки для фильтров
# ТБ
allTb = data['ТБ'].unique()
# Зоны простоя
typeUs = data['Тип УС'].unique()

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    # html.A(
                    #     html.Img(
                    #         src=app.get_asset_url("s1200.png"),
                    #         className="logo",
                    #     ),
                    #     href="https://plotly.com/dash",
                    # ),
                    # html.A(
                    #     html.Button(
                    #         "Enterprise Demo",
                    #         id="learn-more-button",
                    #         style={"margin-left": "-10px"},
                    #     ),
                    #     #href="https://plotly.com/get-demo/",
                    # ),
                    # html.A(
                    #     html.Button("Source Code", id="learn-more-button"),
                    #     #href="https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Статистика доступости сети устройств самообслуживания")],
                        className="seven columns main-title",
                    ),
                    # html.Div(
                    #     [
                    #         dcc.Link(
                    #             "Full View",
                    #             href="/dash-financial-report/full-view",
                    #             className="full-view-link",
                    #         )
                    #     ],
                    #     className="five columns",
                    # ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Price Performance",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Portfolio & Management",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Fees & Minimums", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Distributions",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

# Расчет ФРВ для конкретного банка
def frvTimeСalculation(tb=allTb):
    frvTime=[]
    for i in tb:
        frvTime.append(sum(data.loc[data['ТБ'].isin(tb)]['ФРВ']))
    return frvTime


# Рсчет простоев по всей сети или отделбному банку по всем зонам или отделбной зоне простоя
def downTimeСalculation(tb=allTb, typeUs=typeUs):
    downTime = []
    # downTime = data.loc[(data['ТБ'].isin(tb)) & (data['Тип УС'].isin(typeUs))]['Простой']
    for i in tb:
        downTime.append(sum(data.loc[(data['ТБ'].isin(tb)) & (data['Тип УС'].isin(typeUs))]['Простой']))
    return downTime


# Расчет доступности сети
def availabilityTimeСalculation(tb=allTb, typeUs=typeUs):
    availabilityTime = np.around([(1 - a/b)*100 for a, b in zip(downTimeСalculation(tb, typeUs), frvTimeСalculation(tb))], decimals=2)
    return availabilityTime
