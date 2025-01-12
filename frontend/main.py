import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_ENDPOINT = os.environ.get("API_ENDPOINT")

@st.dialog("Add Post", width="large")
def add_post():
    title = st.text_input("Title")
    tags = st.text_input("Tags")
    content = st.text_area("Content")

    if st.button("Submit"):
        data = {
            "title" : title,
            "tags" : [ tag.strip() for tag in tags.split(",") ],
            "content" : content
        }
        st.write(data)
        response = requests.post(f'{API_ENDPOINT}/posts', data=json.dumps(data))
        if not response.ok:
            st.write(response.reason)
        else:
            st.rerun()

@st.dialog("Edit Post", width="large")
def edit_post(id: str, title: str, tags: list[str], content: str):
    title_input = st.text_input("Title", title)
    tags_input = st.text_input("Tags", tags)
    content_input = st.text_area("Content", content)

    col1, col2, col3 = st.columns([1.6, 1.5, 10])
    with col1:
        if st.button("Submit", type="primary"):
            data = {
                "title" : title_input,
                "tags" : [ tag.strip() for tag in tags_input.split(",") ],
                "content" : content_input
            }
            response = requests.put(f'{API_ENDPOINT}/posts/{id}', data=json.dumps(data))
            if not response.ok:
                st.write(response.reason)
            else:
                st.rerun()
    with col2:
        if st.button("Close"):
            st.rerun()

@st.dialog("Delete Post")
def delete_post(id: str):
    st.write("Are you sure you want to delete this post?")

    col1, col2, col3 = st.columns([1.75, 1.75, 10])
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
    col1, col2, col3 = st.columns([1, 3, 1], vertical_alignment="bottom")
    with col1:
        st.write("# Blog")
    with col3:
        if st.button("Add Post", type="primary", use_container_width=True):
            add_post()

def show_posts():
    response = requests.get(f"{API_ENDPOINT}/posts")
    data = response.json()

    for post in data:
        st.write(f"### {post['title']}")

        tags = [ f"`{tag}`" for tag in post['tags'] ]
        tags_string = ', '.join(tags)
        st.write(f"Tags: {tags_string}")

        st.markdown(post['content'])

        st.button(
            "Edit",
            key= f'{post['id']}-edit',
            on_click=edit_post,
            args=(
                post['id'],
                post['title'],
                ', '.join(post['tags']),
                post['content']
            )
        )
        st.button(
            "Delete",
            key=f'{post['id']}-delete',
            on_click=delete_post,
            args=(post['id'],)
        )

        st.write("###")

def main():
    show_title()
    show_posts()

if __name__ == "__main__":
    main()
