from fastapi import FastAPI , Request
from routes import calculator_router

app =FastAPI()
app.include_router(calculator_router)

"""
Features and Routes:
Arithmetic Operations (/calculate)
Request body: Accepts an operation (add, subtract, multiply, divide) and two operands.
Response: The result of the arithmetic operation.
Include validations for divide operation to handle division by zero.


"""