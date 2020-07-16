# Coronavirus Counter
import pandas as pd
import numpy as np
import streamlit as st
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/india/"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div", class_ = "maincounter-number")

st.title('Coronavirus Cases (India)')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'Total Cases': pd.Series(data[0].text.strip()),
    'Total Deaths': pd.Series(data[1].text.strip()),
    'Total Recovered': pd.Series(data[2].text.strip())
}))

user_input = st.text_input("label goes here")

st.write(user_input)