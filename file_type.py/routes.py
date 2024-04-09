from fastapi import APIRouter , UploadFile , File, Depends , Form , HTTPException
from typing import Annotated
from model import User , CreateUser 
from sqlmodel import Session , select
from deps import get_db
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router=APIRouter()


@router.post("/register")
async def create_user(user:CreateUser , db:Annotated[Session, Depends(get_db)]):
    user_1 =User(**user.model_dump())
    db.add(user_1)
    db.commit()
    # session.refresh(user_1)
    # session.close()
    
    new_user = {"user_name":user.user_name, "password":user.password , "email":user.email }

    response = {"message": "success" , "data": jsonable_encoder(new_user)}
    
    return JSONResponse (status_code =201 , content = response)
    
    
 


@router.get("/user")
def read_user(session:Annotated[Session, Depends(get_session)]):
   
    user = session.exec( select(User)).all()
    if not user:
        raise HTTPException(status_code=404, detail="Hero not found")
    return user
    