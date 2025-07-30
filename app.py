import streamlit as st
import pandas as pd
from scrapper import scrape_all
from datetime import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata') #timezone to india
ist_time = datetime.now(ist)

st.set_page_config(page_title="Stock Market News Aggregator", layout="wide") #layout

st.title("📈 Stock Market News Aggregator")
st.markdown("Aggregates headlines from **Moneycontrol** and **Economic Times**.") #title

if st.button("Scrape Latest News"):
    with st.spinner("Scraping news articles..."):
        df = scrape_all() #calls scrapper.py
        st.success(f"Scraped {len(df)} articles!")
        st.dataframe(df[['source', 'headline', 'summary', 'link', 'timestamp']])
else:
    st.info("Click the button above to scrape the latest news.")

if st.checkbox("Show saved CSV"):
    df = pd.read_csv("headlines.csv") #for csv creation
    st.dataframe(df[['source', 'headline', 'summary', 'link', 'timestamp']])

st.caption(f"🕒 Last updated: {ist_time.strftime('%Y-%m-%d %H:%M:%S')} IST") #caption date and time at bottom
