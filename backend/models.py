from pydantic import BaseModel

class Post(BaseModel):
    title: str
    tags: list[str]
    content: str
