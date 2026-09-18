from datetime import date, timedelta
import pandas as pd
import plotly.express as px
import streamlit as st
import yfinance as yf

END = date.today() - timedelta(days=1)
START = date.today() - timedelta(days=365)

st.set_page_config(layout="wide", 
                   page_title="Stock Analysis", page_icon="📈")
st.title("Stock Analysis")

st.sidebar.title("Inputs")
ticker = st.sidebar.text_input("Enter stock ticker symbol",
                               value="AAPL", max_chars=5).upper()
col1, col2 = st.sidebar.columns(2)
start_date = col1.date_input("Start date", START)
end_date = col2.date_input("End date", END)
mv_avg = st.sidebar.slider("Moving average window",
                           min_value= 1,
                             max_value= 100,
                               value= 50,
                               step= 1)
run_analysis = st.sidebar.button("Run Analysis", type="primary")

def get_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            return None, f"No data found for ticker symbol '{ticker}'"
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            return data, f"Sucessfully downloaded data {ticker} from {start_date} to {end_date}"
    except Exception as e:
        return None, f"Download failed due to {e}"


if run_analysis:
    get_stock_data(ticker, start_date, end_date)