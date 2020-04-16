import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

import pandas as pd
import datetime

@st.cache
def get_data():
    return pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

figure_placeholder = st.empty()

df = get_data()

min_date = pd.to_datetime(df.Date).min().date()
max_date = pd.to_datetime(df.Date).max().date()
day_range = (max_date - min_date).days

bottom_day, top_day = st.slider(label="Date selector",
                                min_value=0,
                                max_value=day_range,
                                value=(0, day_range),
                                step=1,
                                format="%d years old")
bottom_date = min_date + datetime.timedelta(bottom_day)
top_date = min_date + datetime.timedelta(top_day)
st.write("Bottom date: ", bottom_date)
st.write("Top date: ", top_date)

new_df = df[df.Date.between(bottom_date.isoformat(), top_date.isoformat())]

fig = go.Figure(data=[go.Candlestick(x=new_df['Date'],
                                     open=new_df['AAPL.Open'],
                                     high=new_df['AAPL.High'],
                                     low=new_df['AAPL.Low'],
                                     close=new_df['AAPL.Close'])])

fig.update_layout(xaxis_rangeslider_visible=False)


figure_placeholder.plotly_chart(fig)
