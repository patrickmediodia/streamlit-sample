import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = os.environ.get("API_ENDPOINT")

@st.dialog("Add Post")
def add_post():
    title = st.text_input("Title")
    tags = st.text_input("Tags")
    content = st.text_area("Content")

    if not st.button("Submit"):
        data = {
            "title" : title,
            "tags" : tags.split(","),
            "content" : content
        }
        st.write(data)
        response = requests.post(f'{API_ENDPOINT}/posts', data=json.dumps(data))
        if not response.ok:
            st.write(response.reason)
        else:
            st.rerun()

@st.dialog("Delete Post")
def delete_post(id):
    st.write("Are you sure you want to delete this post?")

    col1, col2, col3 = st.columns([1, 1, 5], vertical_alignment="bottom")
    with col1:
        if st.button("Yes", type="primary"):
            response = requests.delete(f"{API_ENDPOINT}/posts/{id}")
            if not response.ok:
                st.write(response.reason)
            else:
                st.rerun()

    with col2:
        if st.button("No"):
            st.rerun()

def show_title():
    col1, col2 = st.columns([6, 1], vertical_alignment="bottom")
    with col1:
        st.write("# Blog")
    with col2:
        if st.button("Add Post", type="primary"):
            add_post()

def show_posts():
    response = requests.get(f"{API_ENDPOINT}/posts")
    data = response.json()

    for post in data:
        col1, col2 = st.columns([20, 1], vertical_alignment="bottom")
        with col1:
            st.write(f"### {post['title']}")
        with col2:
            if st.button("x", key=post['id'], type="tertiary"):
                delete_post(post['id'])

        tags = [ f"`{tag}`" for tag in post['tags'] ]
        tags_string = ', '.join(tags)
        st.write(f"Tags: {tags_string}")

        st.markdown(post['content'])

def main():
    show_title()
    show_posts()

if __name__ == "__main__":
    main()
