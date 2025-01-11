from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello, world!"

@app.get("/table")
def get_table():
    return [
        {
            "id": 0,
            "name": "name",
            "group": "group",
            "cron_expression" : "cron_expression",
            "status": "status",
            "description" : "description"
        },
        {
            "id": 1,
            "name": "name",
            "group": "group",
            "cron_expression" : "cron_expression",
            "status": "status",
            "description" : "description"
        },
        {
            "id": 2,
            "name": "name",
            "group": "group",
            "cron_expression" : "cron_expression",
            "status": "status",
            "description" : "description"
        },
    ]
