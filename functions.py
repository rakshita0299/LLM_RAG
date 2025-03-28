import os
import webbrowser
import psutil
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Predefined Functions
def open_chrome():
    """Opens Google Chrome."""
    logging.info("Executing: open_chrome()")
    webbrowser.open("https://www.google.com")

def open_calculator():
    """Opens Calculator."""
    logging.info("Executing: open_calculator()")
    os.system("calc")

def get_cpu_usage():
    """Returns CPU usage percentage."""
    logging.info("Executing: get_cpu_usage()")
    return f"CPU Usage: {psutil.cpu_percent()}%"

def get_ram_usage():
    """Returns RAM usage percentage."""
    logging.info("Executing: get_ram_usage()")
    return f"RAM Usage: {psutil.virtual_memory().percent}%"

# Function Registry (Predefined)
FUNCTIONS = {
    "Open Google Chrome browser": open_chrome,
    "Open the system calculator": open_calculator,
    "Get the current CPU usage": get_cpu_usage,
    "Get the current RAM usage": get_ram_usage,
}

# Allow users to dynamically add functions
def add_function(name, func_code):
    """Adds a new function dynamically to the system."""
    if name in FUNCTIONS:
        raise ValueError(f"Function '{name}' already exists!")

    exec(func_code, globals())  # Execute function code
    new_func = globals().get(name)  # Retrieve function reference

    if not callable(new_func):
        raise ValueError("Invalid function definition.")

    FUNCTIONS[name] = new_func  # Add function to registry
    logging.info(f"New function added: {name}")
