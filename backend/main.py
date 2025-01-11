import json
from models import Post
from fastapi import FastAPI
from db import get_posts, write_posts

app = FastAPI()

@app.get("/posts")
async def get_posts_route():
    return get_posts()

@app.get("/posts/{id}")
async def get_post_route(id: int):
    posts = get_posts()
    for post in posts:
        if post['id'] == id:
            return post
    else:
        return { "error": "Post not found" }

@app.post("/posts")
async def post_post_route(post: Post):
    posts = get_posts()
    posts.append(post)
    write_posts(posts)

@app.put("/posts/{id}")
async def put_post_route(post: Post):
    posts = get_posts()
    for i, p in enumerate(posts):
        if p['id'] == post.id:
            posts[i] = post
            write_posts(posts)
            return post
    else:
        return { "error": "Post not found" }
