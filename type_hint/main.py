from fastapi import FastAPI, Query
from typing import List, Dict, Tuple, Set, Any, Optional, Union

app = FastAPI() 

@app.get("/dataitems/")
async def read_items(data: Union[int, str]):
    return data

@app.get("/items/")
async def read_items(q: List[int]= Query([1, 2])):
    return {"q": q}

@app.post("/create-item/")
async def create_item(item: Any):
    return item