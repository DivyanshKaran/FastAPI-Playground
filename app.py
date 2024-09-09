from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# The most simple FastAPI route
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


@app.get("/div")
async def id():
    return {"message": f"This is to show that order matters in FastAPI because code will start reading from top"}

# this defines how we get ids from the url
@app.get("/{name}")
async def name(name: str):
    return {"message": f"FastAPI says hello to {name}"}

# You cannot redifine paths since the top path will alwayds be read


# How to use Enum class with code
class Models(str,Enum):
    deeplavv3 = "deeplavv3"
    segnet = "segnet"
    pspnet = "pspnet"

@app.get("/models/{model}")
async def model(model: Models):
    if model is Models.deeplavv3:
        return {"message": "Divyansh Works on this model","model": model}
    if model is Models.segnet:
        return {"message": "Harsh works on this model","model": model}
    if model.value == "pspnet":
        return {"message": "Jai works on this model", "model": model}
    return {"message": "We don't know this model","model": "none"}

# This is to show query parameters
@app.get("/query/")
async def query(height: int=180,weight: int=80,name: str="divyansh", grade: str | None = None ):
    if grade is not None:
        return {"message": f"Your name is {name} and your height is {height} and your weight is {weight}and your grade is {grade}"}
    return {"message": f"Your name is {name} and your height is {height} and your weight is {weight}"}

# we can declare the multiple variables in any order we want
@app.get("/{id}/items/{name}")
async def read(id:int ,name: str,grade: str | None = None):
    return {"message": f"{name} with student {id}"}
