from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import LineTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import LineTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Line Type"],prefix="/api/general")

@router.get("/get-line-types", status_code=200)
def get_line_types(db:Session=Depends(get_db)):
    line_types = LineTypeCrud.get_line_types_cruds(db,0,100)
    if not line_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),line_types)

@router.get("/get-line-type/{line_type_id}", status_code=200)
def get_line_type(line_type_id, db:Session=Depends(get_db)):
    line_type = LineTypeCrud.get_line_type_cruds(db, line_type_id)
    if not line_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),line_type)

@router.post("/create-line-type", status_code=201)
def post_line_type(payload:LineTypeSchema.MtrLineTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_line_type = LineTypeCrud.post_line_type_cruds(db, payload)
        db.add(new_line_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_line_type)
    return CommonResponse.payload(ResponseException(201), new_line_type)

@router.delete("/delete-line-type/{line_type_id}", status_code=202)
def delete_line_type(line_type_id, db:Session=Depends(get_db)):
    erase_line_type = LineTypeCrud.delete_line_type_cruds(db,line_type_id)
    if not erase_line_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_line_type)

@router.put("/update-line-type/{line_type_id}", status_code=202)
def put_line_type(payload:LineTypeSchema.MtrLineTypeGetSchema, line_type_id,db:Session=Depends(get_db)):
    update_line_type, update_data_new  = LineTypeCrud.put_line_type_cruds(db,payload, line_type_id)
    if not update_line_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-line-type/{line_type_id}", status_code=202)
def patch_line_type(line_type_id,db:Session=Depends(get_db)):
    active_line_type  = LineTypeCrud.patch_line_type_cruds(db, line_type_id)
    if not active_line_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_line_type.is_active = not active_line_type.is_active
    db.commit()
    db.refresh(active_line_type)
    return CommonResponse.payload(ResponseException(200), active_line_type.is_active)