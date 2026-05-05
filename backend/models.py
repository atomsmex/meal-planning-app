from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    recipes = relationship('Recipe', back_populates='owner')
    meal_plans = relationship('MealPlan', back_populates='owner')

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='recipes')

class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='meal_plans')
    items = relationship('MealPlanItem', back_populates='meal_plan')

class MealPlanItem(Base):
    __tablename__ = 'meal_plan_items'

    id = Column(Integer, primary_key=True)
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    meal_plan = relationship('MealPlan', back_populates='items')
    recipe = relationship('Recipe')

class ShoppingList(Base):
    __tablename__ = 'shopping_lists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User')