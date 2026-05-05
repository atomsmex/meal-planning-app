from fastapi import APIRouter, HTTPException
from typing import List, Optional

router = APIRouter()

# Sample in-memory recipe database
recipes_db = [
    {"id": 1, "name": "Spaghetti Bolognese", "ingredients": ["spaghetti", "beef", "tomato sauce"], "instructions": "Cook spaghetti and mix with sauce."},
    {"id": 2, "name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk"], "instructions": "Cook chicken and add spices."}
]

@router.get("/recipes", response_model=List[dict])
async def search_recipes(name: Optional[str] = None):
    results = recipes_db
    if name:
        results = [recipe for recipe in recipes_db if name.lower() in recipe['name'].lower()]
    return results

@router.get("/recipes/{recipe_id}", response_model=dict)
async def get_recipe(recipe_id: int):
    recipe = next((recipe for recipe in recipes_db if recipe['id'] == recipe_id), None)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

# Include the router in your FastAPI app
# app.include_router(router)
