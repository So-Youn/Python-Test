from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# def my_func(x:int) -> int:  return int

# http method
@app.get('/')
async def hello_world():
    return {"Hello": "World"} # json response - handling url

@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component_id": component_id} 

# create parameter
@app.get("/component/") 
async def read_component(number: int, text: str): # query parameter
    return {"number": number, "text": text}