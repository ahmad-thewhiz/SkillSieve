import time
from datetime import datetime
from typing import List
from dotenv import load_dotenv

# FastAPI Imports
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Custom Imports
from src import services
from database import schemas, databases

# Database Imports
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError


# Load Environment Variables
load_dotenv()


# Database Connection
client = databases.get_client()
database = databases.get_database(client)
users_collection = databases.get_collection(database, "users")
data_collection = databases.get_collection(database, "data")


# FastAPI App
app = FastAPI(
    title="SkillSieve",
    description="SkillSieve is a platform that helps you to find the right candidate for a job description.",
)


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Healthcheck
@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"Response": "Server is Live!"}


# Get User Details
@app.get("/{username}", response_model=schemas.user_details)
def get_user_details(username: str):
    user = users_collection.find_one({"username": username})
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found") 
    
    return user


# Register User
@app.post("/register", response_model=schemas.register_response)
def register_user(user_details: schemas.register_request):
    try:
        users_collection.insert_one(
            {
                "username": user_details.username,
                "name": user_details.name,
                "email": user_details.email,
                "password": user_details.password,
                "total_generations": 0
            }
        )
        return {"username": user_details.username, "status": "User Registered Successfully"}
    
    except DuplicateKeyError:
        return {"username": user_details.username, "status": "User Already Exists"}
    
    except Exception as e:
        raise Exception(f"Error registering user: {e}")
    

# Update User Details
@app.put("/{username}", response_model=schemas.user_details)
def update_user_details(username: str, user_details: schemas.update_user_details):
    user = users_collection.find_one({"username": username})
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found") 
    
    if user_details.name == user["name"] and user_details.email == user["email"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No changes to update")

    users_collection.update_one(
        {"username": username},
        {"$set": {"name": user_details.name, "email": user_details.email}}
    )

    updated_user = users_collection.find_one({"username": username})
    
    return updated_user


# Delete User
@app.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(username: str):
    user = users_collection.find_one({"username": username})
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found") 
    
    users_collection.delete_one({"username": username})
    
    return None


# Get History
@app.get("/history/{username}", response_model=List[schemas.run_response])
def get_history(username: str):
    user = users_collection.find_one({"username": username})
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found") 
    
    data = list(data_collection.find({"username": username}).sort("timestamp", ASCENDING))
    
    for doc in data:
        doc.pop("_id")

    return data


# Run Agent
@app.get("/run/{username}", response_model=schemas.run_response)
def run_agent(username: str, query: str):

    user = users_collection.find_one({"username": username})

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    
    start_time = time.time()

    inputs = {
        "job_requirements": query
    }

    output = services.run(inputs)
    
    time_taken = time.time() - start_time

    current_date_time = datetime.now()
    current_date_time_str = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    try:
        data_collection.insert_one({
            "username": username,
            "process_type": "run",
            "query": query,
            "response": output,
            "time_taken": time_taken,
            "timestamp": current_date_time_str
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail= f"An error occurred while trying to save data {e}")

    users_collection.update_one({"username": "ahmad4raza"}, {"$inc": {"total_generations": 1}})

    return {"username": username, "process_type": "run", "query": query, "response": output, "time_taken": time_taken, "timestamp": current_date_time_str}


# Train Agent
@app.get("/train/{username}", response_model=schemas.train_response)
def train_agent(username: str, train_details: schemas.train_request):
    
    user = users_collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    
    start_time = time.time()
    
    inputs = {
        "job_requirements": train_details.query,
    }
    output = services.train(inputs=inputs, n_iterations=train_details.num_of_iterations)
    
    time_taken = time.time() - start_time

    current_date_time = datetime.now()
    current_date_time_str = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    try:
        data_collection.insert_one({
            "username": username,
            "process_type": "train",
            "query": train_details.query,
            "num_iterations": train_details.num_of_iterations,
            "response": output,
            "time_taken": time_taken,
            "timestamp": current_date_time_str
        })
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail= f"An error occurred while trying to save data {e}")

    users_collection.update_one({"username": "ahmad4raza"}, {"$inc": {"total_generations": 1}})

    return {"username": username, "process_type": "train", "query": train_details.query, "num_iterations": train_details.num_of_iterations ,"response": output, "time_taken": time_taken, "timestamp": current_date_time_str}
