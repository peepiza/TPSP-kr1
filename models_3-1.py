from pydantic import BaseModel
from typing import List, Optional

class User1(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str
    message: str