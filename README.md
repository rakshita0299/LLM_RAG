# Dynamic Automation API with LLM + RAG

Welcome to the **Dynamic Automation API**! This project is a Python-based API service that leverages **Retrieval-Augmented Generation (RAG)** and **FastAPI** to dynamically retrieve and execute automation functions based on user prompts. 

## Features
- **AI-powered function matching** using **Sentence Transformers + FAISS**.
- **Fast function execution** for system automation.
- **Dynamic function addition** at runtime.
- **REST API support** via FastAPI.
- **Prebuilt system utilities** (e.g., CPU usage, open apps, etc.).

---

## Project Structure

```
project_root
├── api.py              # FastAPI backend
├── functions.py        # Predefined + user-defined functions
├── vector_store.py     # Function retrieval using FAISS
└── README.md           # Project documentation
```

---

## How It Works

### 1. Function Execution Flow (`/execute`)
1. A **user sends a request** with a prompt (e.g., "Check my RAM usage").
2. **Vector search (FAISS)** finds the **best-matching function**.
3. The **retrieved function is executed** and the result is returned.

#### Example Request:
```json
POST /execute
{
    "prompt": "Get my current CPU usage"
}
```
#### Example Response:
```json
{
    "function": "Get the current CPU usage",
    "message": "Success",
    "execution_time": "0.002 seconds",
    "output": "CPU Usage: 30%"
}
```

---

### 2. Adding New Functions (`/add_function`)
Want to add your own automation function? The API allows users to dynamically add new functions at runtime.

#### Example Request:
```json
POST /add_function
{
    "name": "get_disk_usage",
    "code": "def get_disk_usage(): return 'Disk Usage: 40%'"
}
```
#### Example Response:
```json
{
    "message": "Function 'get_disk_usage' added successfully!"
}
```

---

## Technology Stack
- **FastAPI** - API framework
- **FAISS** - Vector search for function retrieval
- **Sentence Transformers** - Converts text into embeddings
- **Python (psutil, os, webbrowser)** - System automation

---

## Dependencies
To run this project, you need to install the following dependencies:
```sh
pip install fastapi pydantic sentence-transformers faiss-cpu psutil uvicorn
```

---

## Inside the Code
### 1. API Endpoints (api.py)
- `/execute`: Matches the best function and executes it.
- `/add_function`: Allows adding new automation functions dynamically.

### 2. Function Execution (functions.py)
- Predefined automation functions like `open_chrome()`, `get_cpu_usage()`, etc.
- Supports adding functions dynamically using `exec()`.

### 3. Function Matching (vector_store.py)
- **Sentence Transformers** encode function descriptions into vector embeddings.
- **FAISS index** stores and retrieves the most relevant function.

---

## Security Considerations
> **WARNING:** The use of `exec()` to dynamically execute user-provided code can be a **security risk**. Consider sandboxing or validating function inputs before execution.

---

## Future Improvements
- Secure execution of user-defined functions.
- Web-based UI for function management.
- Expand automation capabilities with external integrations.

---

## Getting Started
### 1. Install Dependencies
```sh
pip install fastapi pydantic sentence-transformers faiss-cpu psutil uvicorn
```

### 2. Run the API
```sh
uvicorn api:app --reload
```

### 3. Test the Endpoints
- Open `http://127.0.0.1:8000/docs` for an interactive API UI.

---

## License
This project is **open-source** and available under the **MIT License**.

---

### Contributions Welcome!
Feel free to **fork** this repo, **submit issues**, and **improve** the project!

