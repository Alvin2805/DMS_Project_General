from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import BrandTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import BrandTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Brand Type"],prefix="/api/general")

@router.get("/get-brand-types", status_code=200)
def get_brand_types(db:Session=Depends(get_db)):
    brand_types = BrandTypeCrud.get_brand_types_cruds(db,0,100)
    if not brand_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),brand_types)

@router.get("/get-brand-type/{brand_type_id}", status_code=200)
def get_brand_type(brand_type_id, db:Session=Depends(get_db)):
    brand_type = BrandTypeCrud.get_brand_type_cruds(db, brand_type_id)
    if not brand_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),brand_type)

@router.post("/create-brand-type", status_code=201)
def post_brand_type(payload:BrandTypeSchema.MtrBrandTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_brand_type = BrandTypeCrud.post_brand_type_cruds(db, payload)
        db.add(new_brand_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_brand_type)
    return CommonResponse.payload(ResponseException(201), new_brand_type)

@router.delete("/delete-brand-type/{brand_type_id}", status_code=202)
def delete_brand_type(brand_type_id, db:Session=Depends(get_db)):
    erase_brand_type = BrandTypeCrud.delete_brand_type_cruds(db,brand_type_id)
    if not erase_brand_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_brand_type)

@router.put("/update-brand-type/{brand_type_id}", status_code=202)
def put_brand_type(payload:BrandTypeSchema.MtrBrandTypeGetSchema, brand_type_id,db:Session=Depends(get_db)):
    update_brand_type, update_data_new  = BrandTypeCrud.put_brand_type_cruds(db,payload, brand_type_id)
    if not update_brand_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-brand-type/{brand_type_id}", status_code=202)
def patch_brand_type(brand_type_id,db:Session=Depends(get_db)):
    active_brand_type  = BrandTypeCrud.patch_brand_type_cruds(db, brand_type_id)
    if not active_brand_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_brand_type.is_active = not active_brand_type.is_active
    db.commit()
    db.refresh(active_brand_type)
    return CommonResponse.payload(ResponseException(200), active_brand_type.is_active)