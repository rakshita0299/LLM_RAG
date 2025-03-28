from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions import FUNCTIONS, add_function
from vector_store import retrieve_best_function, update_function_store
import logging
import time

# Initialize FastAPI
app = FastAPI()

# Request Models
class RequestBody(BaseModel):
    prompt: str

class CustomFunction(BaseModel):
    name: str
    code: str

@app.post("/execute")
def execute_function(request: RequestBody):
    """Processes user input, retrieves a function, logs, and executes it."""
    best_function_name = retrieve_best_function(request.prompt)

    if best_function_name not in FUNCTIONS:
        logging.warning(f"No matching function found for: {request.prompt}")
        raise HTTPException(status_code=404, detail="No matching function found.")

    best_function = FUNCTIONS[best_function_name]

    logging.info(f"Function matched: {best_function_name}")

    start_time = time.time()
    try:
        result = best_function()  # Execute retrieved function
        execution_time = round(time.time() - start_time, 4)
        logging.info(f"Executed '{best_function_name}' in {execution_time}s.")

        return {
            "function": best_function_name,
            "message": "Success",
            "execution_time": f"{execution_time} seconds",
            "output": result if result else "No output"
        }
    except Exception as e:
        logging.error(f"Execution failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/add_function")
def add_custom_function(request: CustomFunction):
    """Allows users to define and add new functions dynamically."""
    try:
        add_function(request.name, request.code)  #  Add new function
        update_function_store()  #  Update FAISS index
        return {"message": f"Function '{request.name}' added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding function: {e}")
