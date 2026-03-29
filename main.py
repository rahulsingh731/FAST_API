from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="Items Manager API",
    description="A simple API to manage items",
    version="1.0.0"
)

# Pydantic Models
class Item(BaseModel):
    """Item model for request/response validation"""
    name: str = Field(..., min_length=1, max_length=100, description="Name of the item")
    description: str = Field(default="", max_length=500, description="Item description")
    price: float = Field(default=0.0, ge=0, description="Item price")

    class Config:
        schema_extra = {
            "example": {
                "name": "Apple",
                "description": "Fresh red apple",
                "price": 1.99
            }
        }


class ItemResponse(BaseModel):
    """Response model for item operations"""
    id: int
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "item": {
                    "name": "Apple",
                    "description": "Fresh red apple",
                    "price": 1.99
                }
            }
        }


# In-memory storage
items: List[Item] = []


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to Items Manager API", "author": "Rahul"}


@app.post("/items", response_model=List[Item])
def create_item(item: Item):
    """Create a new item"""
    items.append(item)
    return items


@app.get("/items", response_model=List[Item])
def list_items(limit: int = 10):
    """Get all items with optional limit"""
    return items[:limit]


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    """Get item by ID"""
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    return {"id": item_id, "item": items[item_id]}


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated_item: Item):
    """Update an item by ID"""
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    items[item_id] = updated_item
    return {"id": item_id, "item": items[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by ID"""
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    deleted_item = items.pop(item_id)
    return {"message": f"Item deleted", "deleted_item": deleted_item, "remaining_items": len(items)}

@app.get("/items")
def list_items(limit:int=10):
    return items[0:limit]
