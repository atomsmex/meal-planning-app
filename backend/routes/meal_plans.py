from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class MealPlan(BaseModel):
    day: str
    meals: List[str]

class WeeklyMealPlan(BaseModel):
    week: str
    plans: List[MealPlan]

meal_plans = {}  # Dictionary to store meal plans by week

@router.post("/meal-plans/", response_model=WeeklyMealPlan)
async def create_meal_plan(weekly_meal_plan: WeeklyMealPlan):
    meal_plans[weekly_meal_plan.week] = weekly_meal_plan
    return weekly_meal_plan

@router.put("/meal-plans/{week}/", response_model=WeeklyMealPlan)
async def update_meal_plan(week: str, weekly_meal_plan: WeeklyMealPlan):
    if week not in meal_plans:
        raise HTTPException(status_code=404, detail="Meal plan not found")
    meal_plans[week] = weekly_meal_plan
    return weekly_meal_plan

@router.get("/meal-plans/{week}/", response_model=WeeklyMealPlan)
async def get_meal_plan(week: str):
    if week not in meal_plans:
        raise HTTPException(status_code=404, detail="Meal plan not found")
    return meal_plans[week]
