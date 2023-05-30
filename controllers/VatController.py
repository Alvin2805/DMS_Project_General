from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import VatCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import VatSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Vat Company"],prefix="/api/general")

@router.get("/vat-company", status_code=200)
def get_all(db:Session=Depends(get_db)):
    results = VatCrud.get_vat_companies(db,0,100)
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),results)

@router.get("/vat-company/{vat_id}", status_code=200)
def get_by_id(vat_id:int, db:Session=Depends(get_db)):
    result = VatCrud.get_vat_company(db, vat_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),result)

@router.post("/vat-company", status_code=201)
def post_data(payload:VatSchema.VatCompanySchema,db:Session=Depends(get_db)):
    try:
        new_data = VatCrud.post_vat_company(db, payload)
        db.add(new_data)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_data)
    return CommonResponse.payload(ResponseException(201), new_data)

@router.delete("/vat-company/{vat_id}", status_code=202)
def delete_vat_company(vat_id:int, db:Session=Depends(get_db)):
    delete_data = VatCrud.delete_vat_company(db,vat)
    if not delete_data:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), delete_data)

@router.put("/vat-company/{vat_id}", status_code=202)
def put_vat_company(payload:VatSchema.VatCompanySchema, vat_id:int,db:Session=Depends(get_db)):
    update_vatcompany, update_data_new  = VatCrud.put_vat_company(db,payload, vat_id)
    if not update_vatcompany:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/vat-company/{vat_id}", status_code=202)
def patch_vat_company(vat_id:int,db:Session=Depends(get_db)):
    active_vat_company  = VatCrud.patch_vat_company(db, vat_id)
    if not active_vat_company:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_vat_company.is_active = not active_vat_company.is_active
    db.commit()
    db.refresh(active_vat_company)
    return CommonResponse.payload(ResponseException(200), active_vat_company.is_active)