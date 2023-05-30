from fastapi import APIRouter,Depends,HTTPException,status
from src.payloads import CommonResponse
from src.exceptions.RequestException import ResponseException 
from src.cruds import LoggingCrud
from src.schemas import LoggingSchema
from starlette.requests import Request
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db

router = APIRouter(tags=["Logging"],prefix="/api/general")

@router.get("/get-loggings", status_code=200)
def get_loggings(db:Session=Depends(get_db)):
    loggings = LoggingCrud.get_loggings_cruds(db,0,100)
    if not loggings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),loggings)

@router.get("/get-logging/{logging_id}", status_code=status.HTTP_200_OK)
def get_logging(logging_id, db:Session=Depends(get_db)):
    logging = LoggingCrud.get_logging_cruds(db, logging_id)
    if not logging:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200), logging)

@router.post("/create-logging", status_code=201)
def post_logging(payload:LoggingSchema.MtrLoggingPostSchema,db:Session=Depends(get_db)):
    try :
        new_logging = LoggingCrud.post_logging_cruds(db, payload)
        new_logging.created_at = datetime.now()
        new_logging.created_by = '150650'
        new_logging.ipaddress = Request.client.host
        db.add(new_logging)
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_logging)
    return CommonResponse.payload(ResponseException(201), new_logging)

@router.delete("/delete-logging/{logging_id}", status_code=202)
def delete_logging(logging_id, db:Session=Depends(get_db)):
    erase_logging = LoggingCrud.delete_logging_cruds(db,logging_id)
    if not erase_logging:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_logging)

@router.put("/update-logging/{logging_id}", status_code=202)
def put_logging(payload:LoggingSchema.MtrLoggingPutSchema, logging_id,db:Session=Depends(get_db)):
    update_logging, update_data_new  = LoggingCrud.put_logging_cruds(db,payload, logging_id)
    update_logging.changed_at = datetime.now()
    update_logging.changed_by = '150650'
    update_logging.ipaddress = Request.client.host
    if not update_logging:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-logging/{logging_id}", status_code=202)
def patch_logging(logging_id,db:Session=Depends(get_db)):
    active_logging  = LoggingCrud.patch_logging_cruds(db, logging_id)
    if not active_logging:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_logging.is_active = not active_logging.is_active
    db.commit()
    db.refresh(active_logging)
    return CommonResponse.payload(ResponseException(200), active_logging.is_active)
