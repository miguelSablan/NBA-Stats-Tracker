import streamlit as st
import pandas as pd
import numpy as np
import requests as requests

# miguel was here

# Young Money

st.title("NBA Stats Tracker")

option = st.radio("Please select what data you would like to see:",("Player stats", "Team Stats"))

player_searched = ""

player_url = "https://www.balldontlie.io/api/v1/players?search={1}".format(player_searched)

if option == "Player stats":
    st.selectbox("Please type in a player name:")



