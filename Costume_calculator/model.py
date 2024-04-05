from pydantic import BaseModel , Field

class Process(BaseModel):
    first_number:int = Field(description= "supply the first number", examples= 2)
    second_number: int = Field(description = "supply the second number" , examples =3)
    
class Responses(BaseModel):
    status: int
    data: dict
    message: str