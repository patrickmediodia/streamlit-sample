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

    if st.button("Submit"):
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

@st.dialog("Edit Post")
def edit_post(title, tags, content):
    st.text_input("Title").value = title
    st.text_input("Tags").value = tags
    st.text_area("Content").value = content

    if st.button("Submit"):
        data = {
            "title" : st.text_input("Title").value,
            "tags" : st.text_input("Tags").value.split(","),
            "content" : st.text_area("Content").value
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
        col1, col2, col3 = st.columns([16, 1, 1.5], vertical_alignment="bottom")
        with col1:
            st.write(f"### {post['title']}")
        with col2:
            if st.button("Edit", key= f'{post['id']}/edit', type="tertiary"):
                edit_post(post['title'], ', '.join(post['tags']), post['content'])
        with col3:
            if st.button("Delete", key=f'{post['id']}/delete', type="tertiary"):
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
