import os
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_ENDPOINT = os.environ.get("API_ENDPOINT")

def show_posts():
    response = requests.get(f"{API_ENDPOINT}/posts")
    data = response.json()

    for post in data:
        st.write(f"### {post['title']}")
        for tag in post['tags']:
            st.write(f"`{tag}`")
        st.write(post['content'])

def main():
    st.write("# Blog Posts")
    show_posts()

if __name__ == "__main__":
    main()
