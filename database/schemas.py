from pydantic import BaseModel

class register_request(BaseModel):
    username: str
    name: str
    email: str
    password: str


class register_response(BaseModel):
    username: str
    status: str

    class Config:
        orm_mode = True


class user_details(BaseModel):
    username: str
    name: str
    email: str
    total_generations: int

    class Config:
        orm_mode = True


class update_user_details(BaseModel):
    name: str
    email: str


class run_response(BaseModel):
    username: str
    process_type: str
    query: str
    response: str
    time_taken: float
    timestamp: str
    
    class Config:
        orm_mode = True


class train_request(BaseModel):   
    query: str
    num_of_iterations: int


class train_response(BaseModel):
    username: str
    process_type: str
    query: str
    num_iterations: int
    response: str
    time_taken: float
    timestamp: str
    
    class Config:
        orm_mode = True
