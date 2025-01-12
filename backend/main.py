import uuid
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
    dict_post = post.model_dump()
    dict_post['id'] = str(uuid.uuid4())

    posts = get_posts()
    posts.append(dict_post)

    write_posts(posts)
    return posts

@app.put("/posts/{id}")
async def put_post_route(id: str, post: Post):
    posts = get_posts()

    for i, p in enumerate(posts):
        if p['id'] == id:
            dict_post = post.model_dump()
            dict_post['id'] = id
            posts[i] = dict_post
            write_posts(posts)
            return dict_post
    else:
        return { "error": "Post not found" }

@app.delete("/posts/{id}")
async def delete_post_route(id: str):
    posts = get_posts()

    for i, post in enumerate(posts):
        if post['id'] == id:
            del posts[i]
            write_posts(posts)
            return post
    else:
        return { "error": "Post not found" }
