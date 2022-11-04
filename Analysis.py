from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

def bar_chart():

    # initialize chart

    chart = Chart(width="1040px", height="1060px", display=DisplayTarget.MANUAL)


    # add data

    data = Data()
    data_frame = pd.read_excel("https://github.com/manishthilagar/sample/blob/main/2019%20CRS.xlsx?raw=true")
    data.add_data_frame(data_frame)

    chart.animate(data)


    # add config
    chart.animate(
    Style({"plot": {"marker": {"colorPalette": "#009E60"}}})
)
    chart.animate(Config({"x": "Company", "y": "2019 Efficiency", "label": "2019 Efficiency","title":"Efficiency"}))
    chart.animate(Config({"x": ["Company"], "label": ["2019 Efficiency"]}))
    chart.animate(Config({"x": "Company", "y": ["2019 Efficiency"]}))
    chart.animate(
    Style({"plot": {"marker": {"colorPalette": "#7FFFD4"}}})
)

    chart.animate(Config({"y": "Company", "x": "2019 Efficiency", "label": "2019 Efficiency","title":"Efficiency %"}))
    # add style

    chart.animate(Style({"title": {"fontSize": 35}}))
    chart.animate(Config({"align": "center"}))
    
    chart.animate(
    Config(
        {
            "sort": "byValue",
        }
    )
)
    chart.animate(
    Style({"plot": {"marker": {"colorPalette": "#088F8F"}}})
)

    return chart._repr_html_()
CHART = bar_chart()
html(CHART, width=4350, height=1370)
