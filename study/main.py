from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

@app.get("/items/")
async def read_items(q: List[int]= Query([1, 2])):
    return {"q": q}

@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item