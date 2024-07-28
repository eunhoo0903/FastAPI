from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 경로 매개변수 
@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

# 쿼리 매개변수
@app.get("/items/")
def read_items(skip=0, limit=10):
    return {"skip": skip, "limit": limit}