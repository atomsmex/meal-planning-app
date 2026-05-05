from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Data model for Shopping List
class ShoppingList(BaseModel):
    id: int
    name: str
    items: List[str]

# In-memory database to hold shopping lists
shopping_lists = []

@router.post("/shopping_list/", response_model=ShoppingList)
async def create_shopping_list(list: ShoppingList):
    shopping_lists.append(list)
    return list

@router.get("/shopping_lists/", response_model=List[ShoppingList])
async def get_shopping_lists():
    return shopping_lists

@router.put("/shopping_list/{list_id}", response_model=ShoppingList)
async def update_shopping_list(list_id: int, list: ShoppingList):
    for idx, existing_list in enumerate(shopping_lists):
        if existing_list.id == list_id:
            shopping_lists[idx] = list
            return list
    raise HTTPException(status_code=404, detail="Shopping list not found")

@router.delete("/shopping_list/{list_id}")
async def delete_shopping_list(list_id: int):
    for idx, existing_list in enumerate(shopping_lists):
        if existing_list.id == list_id:
            del shopping_lists[idx]
            return {
                "detail": "Shopping list deleted"
            }
    raise HTTPException(status_code=404, detail="Shopping list not found")
