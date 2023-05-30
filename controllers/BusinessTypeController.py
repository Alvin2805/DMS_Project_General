from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import BusinessTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import BusinessTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Business Type"],prefix="/api/general")

@router.get("/get-business-types", status_code=200)
def get_business_types(db:Session=Depends(get_db)):
    business_typess = BusinessTypeCrud.get_business_types_cruds(db,0,100)
    if not business_typess:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),business_typess)

@router.get("/get-business-type/{business_type_id}", status_code=200)
def get_business_type(business_type_id, db:Session=Depends(get_db)):
    business_type = BusinessTypeCrud.get_business_type_cruds(db, business_type_id)
    if not business_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),business_type)

@router.post("/create-business-type", status_code=201)
def post_business_type(payload:BusinessTypeSchema.MtrBusinessTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_business_type = BusinessTypeCrud.post_business_type_cruds(db, payload)
        db.add(new_business_type)
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_business_type)
    return CommonResponse.payload(ResponseException(201), new_business_type)

@router.delete("/delete-business-type/{business_type_id}", status_code=202)
def delete_business_type(business_type_id, db:Session=Depends(get_db)):
    erase_business_type = BusinessTypeCrud.delete_business_type_cruds(db,business_type_id)
    if not erase_business_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_business_type)

@router.put("/update-business-type/{business_type_id}", status_code=202)
def put_business_type(payload:BusinessTypeSchema.MtrBusinessTypeGetSchema, business_type_id,db:Session=Depends(get_db)):
    update_business_type, update_data_new  = BusinessTypeCrud.put_business_type_cruds(db,payload, business_type_id)
    if not update_business_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-business-type/{business_type_id}", status_code=202)
def patch_business_type(business_type_id,db:Session=Depends(get_db)):
    active_business_type  = BusinessTypeCrud.patch_business_type_cruds(db, business_type_id)
    if not active_business_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_business_type.is_active = not active_business_type.is_active
    db.commit()
    db.refresh(active_business_type)
    return CommonResponse.payload(ResponseException(200), active_business_type.is_active)