from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model import Responses, Process
from services import process_cal

calculator_router =APIRouter(prefix="/calculator", tags=["cal"])
 
@calculator_router.post("/" , response_model=Responses)
async def calculate(process = str):
    results = await process_cal( process)
    return JSONResponse(status_code=201, content={"data": results, "message": "calculation completed"})