import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = os.environ.get("API_ENDPOINT")

data = requests.get(f'{API_ENDPOINT}/table').json()

st.write(data)
