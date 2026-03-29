from fastapi import FastAPI,HTTPException

app = FastAPI()

items = []


@app.get("/")
def read_root():
    return {"Hello": "Rahul"}

@app.post("/items")
def create_item(item:str):
    if item not in items:
        items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    try:
        item = items[item_id]
        return item
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

