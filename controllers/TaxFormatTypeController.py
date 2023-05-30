from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import TaxFormatTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import TaxFormatTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Tax Format Type"],prefix="/api/general")

@router.get("/get-tax-format-types", status_code=200)
def get_tax_format_types(db:Session=Depends(get_db)):
    tax_format_types = TaxFormatTypeCrud.get_tax_format_types_cruds(db,0,100)
    if not tax_format_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),tax_format_types)

@router.get("/get-tax-format-type/{tax_format_type_id}", status_code=200)
def get_tax_format_type(tax_format_type_id, db:Session=Depends(get_db)):
    tax_format_type = TaxFormatTypeCrud.get_tax_format_type_cruds(db, tax_format_type_id)
    if not tax_format_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),tax_format_type)

@router.post("/create-tax-format-type", status_code=201)
def post_tax_format_type(payload:TaxFormatTypeSchema.MtrTaxFormatTypeGetSchema,db:Session=Depends(get_db)):
    try :
        new_tax_format_type = TaxFormatTypeCrud.post_tax_format_type_cruds(db, payload)
        db.add(new_tax_format_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_tax_format_type)
    return CommonResponse.payload(ResponseException(201), new_tax_format_type)

@router.delete("/delete-tax-format-type/{tax_format_type_id}", status_code=202)
def delete_tax_format_type(tax_format_type_id, db:Session=Depends(get_db)):
    erase_tax_format_type = TaxFormatTypeCrud.delete_tax_format_type_cruds(db,tax_format_type_id)
    if not erase_tax_format_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_tax_format_type)

@router.put("/update-tax-format-type/{tax_format_type_id}", status_code=202)
def put_tax_format_type(payload:TaxFormatTypeSchema.MtrTaxFormatTypeGetSchema, tax_format_type_id,db:Session=Depends(get_db)):
    update_tax_format_type, update_data_new  = TaxFormatTypeCrud.put_tax_format_type_cruds(db,payload, tax_format_type_id)
    if not update_tax_format_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-tax-format-type/{tax_format_type_id}", status_code=202)
def patch_tax_format_type(tax_format_type_id,db:Session=Depends(get_db)):
    active_tax_format_type  = TaxFormatTypeCrud.patch_tax_format_type_cruds(db, tax_format_type_id)
    if not active_tax_format_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_tax_format_type.is_active = not active_tax_format_type.is_active
    db.commit()
    db.refresh(active_tax_format_type)
    return CommonResponse.payload(ResponseException(200), active_tax_format_type.is_active)