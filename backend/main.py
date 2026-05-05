from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] ,  # Change to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic route structure
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Meal Planning App!"}

@app.get("/meals")
async def get_meals():
    return [
        {"id": 1, "name": "Chicken Curry"},
        {"id": 2, "name": "Vegetable Stir Fry"}
    ]

@app.post("/meals")
async def create_meal(meal: dict):
    return {"message": "Meal created successfully!", "meal": meal}
