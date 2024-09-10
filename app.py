from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

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

# how to send a Request body

class Item(BaseModel):
    name : str
    description: str | None = None
    price: int

@app.post("/item")
async def getItem(item: Item):
    # print(item)
    # print(item.dict())
    return item

# Additional Validation of query parameteres
from fastapi import Query
from typing import Annotated

@app.get("/items/")
async def read_items(q: Annotated[str | None , Query(min_length=3,max_length=50,pattern="^fixedQuery$")] = "..."):
    results = {}
    if q:
         results.update({"q":q})
    return results

@app.post("/items/")
async def read_item(q: Annotated[list[str]| None,Query(title="Database Call",description="A query to send parameters of the data base call",alias="database-query",deprecated=True,include_in_schema=False)]=["divyansh","karan"]):
    query = {"q":q}
    return query

from fastapi import Path
@app.get("/items/{item_id}/")
async def senditem(item_id: Annotated[int,Path(description="The id of the item to get",ge=10)]):
    return {"message": f"The Item id is {item_id}"}
# To FastAPI it dosent't matter if you declare default values after non default values
# You'd never have problems if you Annnoted