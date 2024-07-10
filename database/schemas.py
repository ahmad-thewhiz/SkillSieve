from pydantic import BaseModel

class run_response(BaseModel):
    username: str
    output: str
    run_time: float

    class Config:
        orm_mode = True

class train_request(BaseModel):   
    job_requirements: str
    num_of_iterations: int

class train_response(BaseModel):
    username: str
    output: str
    train_time: float

    class Config:
        orm_mode = True
