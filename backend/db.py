import json
from models import Post

def get_posts():
    with open('posts.json', 'r') as file:
        data = json.load(file)
    return data

def write_posts(posts: list[Post]):
    with open('posts.json', 'w') as file:
        file.write(json.dumps(posts, indent=4))

