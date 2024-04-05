from fastapi import FastAPI
from pydantic import BaseModel , field_validator
from enum import Enum

app = FastAPI ()

class Operand (str, Enum):
    add = "add"
    sub ="sub"
    mull = "mul"
    div ="div"

class CalcBody (BaseModel):
    operand: Operand
    loperand : float
    roperand : float
    
    @field_validator("operand")
    @classmethod
    def check_operand (cls, value , values):
        if value == "div" and values.data == ["roperand"] ==0:
            raise ValueError ("roperand cannot be zero for division")
        return value
        
    
class Calcresponse (BaseModel):
    result : float
    
@app.post ("/calculate", response_model =Calcresponse)
async def calculate (calc :CalcBody):
    if calc.operand == "add":
        result = calc. loperand + calc.roperand
    elif calc.operand =="sub":
        result = calc.loperand - calc.roperand
    elif calc.operand == "mul":
        result = calc.loperand * calc.roperand
    elif calc.operand == "div":
        result = calc.loperand / calc.roperand
    return {"result": result}
    
    
@app.get("/interest")
async def Calinterest (principal : float , rate : float , time: float  ):
 simple_interest = (principal * rate * time)/(100)
 return  {"simple_intrest" : simple_interest}

@app.get ("/palindrome")
async def Palindrome(text :str):
    for i in range(0, int(len(text)/2)):
        if text[i] != text[len(text)-i-1]:
            return False
    return True