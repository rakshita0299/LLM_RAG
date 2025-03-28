from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions import FUNCTIONS
from vector_store import retrieve_best_function

app = FastAPI()

class RequestBody(BaseModel):
    prompt: str

@app.post("/execute")
def execute_function(request: RequestBody):
    """Processes user input, retrieves a function, and generates Python code."""
    best_function_name, best_function = retrieve_best_function(request.prompt)

    generated_code = f"""
from functions import {best_function.__name__}

def main():
    try:
        result = {best_function.__name__}()  # Call function
        if result:
            print(result)  # Print result if function returns a value
        print("{best_function.__name__} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
    """

    return {
        "function": best_function_name,
        "code": generated_code.strip()
    }
