from fastapi import FastAPI
from pydantic import BaseModel
from generate_text import generate_text

class Item(BaseModel):
    prompt: str


app = FastAPI()

@app.post("/")
async def create_item(item: Item):
    complete = generate_text(item.prompt)
    return complete