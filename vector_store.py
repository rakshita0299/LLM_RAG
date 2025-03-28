from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from functions import FUNCTIONS

# Load Sentence Transformer model (turns text into vectors)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Function descriptions (initially with predefined functions)
function_descriptions = list(FUNCTIONS.keys())

# Encode function descriptions into vector embeddings
function_vectors = model.encode(function_descriptions)

# Store embeddings in FAISS vector index
index = faiss.IndexFlatL2(function_vectors.shape[1])
index.add(np.array(function_vectors))

def update_function_store():
    """Updates FAISS index when new functions are added."""
    global index, function_descriptions
    function_descriptions = list(FUNCTIONS.keys())  # Update function list
    function_vectors = model.encode(function_descriptions)  # Recompute vectors
    index = faiss.IndexFlatL2(function_vectors.shape[1])  # Reset index
    index.add(np.array(function_vectors))  # Add new vectors

def retrieve_best_function(user_prompt):
    """Retrieve the most relevant function using FAISS vector search."""
    query_embedding = model.encode([user_prompt])  # Convert query to vector
    _, indices = index.search(np.array(query_embedding), 1)  # Search FAISS
    best_match = function_descriptions[indices[0][0]]  # Get best-matched function
    return best_match
