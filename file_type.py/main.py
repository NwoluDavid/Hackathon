from fastapi import FastAPI , UploadFile , File
from pydantic import BaseModel , field_validator
from typing import Annotated

app = FastAPI()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content_type = file.content_type 
    return {"filename": file.filename , "file_type": file.content_type}

