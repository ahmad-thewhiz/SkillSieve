import time

# FastAPI Imports
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

# Custom Imports
from src import services
from database import schemas

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

# connect to db

@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"Response": "Server is Live!"}


# @app.post("/register", response_model=schemas.register_response)
# def register_user(user: schemas.register_request):
#     # user registration
#     pass


# @app.post("/login", response_model=schemas.login_response)
# def login_user(user: schemas.login_request):
#     # user login
#     pass


# @app.get("/", response_model=schemas.user_details)
# def get_user_details(username: str):
#     # verify email in the database
#     pass


@app.get("/run/{username}", response_model=schemas.run_response)
def run_agent(username: str, query: str):

    start_time = time.time()
    inputs = {
        "job_requirements": query
    }
    output = services.run(inputs)
    time_taken = time.time() - start_time

    return {"username": username, "output": output, "run_time": time_taken}


@app.get("/train/{username}", response_model=schemas.train_response)
def train_agent(username: str, train_details: schemas.train_request):
    
    start_time = time.time()
    inputs = {
        "job_requirements": train_details.job_requirements,
    }
    output = services.train(inputs=inputs, n_iterations=train_details.num_of_iterations)
    time_taken = time.time() - start_time

    return {"username": username, "output": output, "train_time": time_taken}


# @app.get("/history/{username}", response_model=schemas.history_response)
# def get_history(username: str):
#     # verify email in the database
#     pass