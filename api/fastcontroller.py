# main.py
from fastapi import FastAPI

app = FastAPI()  # Create FastAPI app instance

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI with Uvicorn!"}

# Example endpoint with parameter
@app.get("/square/{number}")
async def square_number(number: int):
    return {"number": number, "square": number**2}

# Example async endpoint
@app.get("/wait")
async def wait_five_seconds():
    import asyncio
    await asyncio.sleep(5)
    return {"message": "Waited 5 seconds asynchronously"}

# FastAPI() → creates the app instance.

# @app.get("/") → defines a GET route.

# Async functions (async def) allow non-blocking requests.

# Path parameters ({number}) are automatically parsed and type-checked.