from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import BankAccountTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import BankAccountTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Bank Account Type"],prefix="/api/general")

@router.get("/get-bank-account-types", status_code=200)
def get_bank_account_types(db:Session=Depends(get_db)):
    bank_account_types = BankAccountTypeCrud.get_bank_account_types_cruds(db,0,100)
    if not bank_account_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),bank_account_types)

@router.get("/get-bank-account-type/{bank_account_type_id}", status_code=200)
def get_bank_account_type(bank_account_type_id, db:Session=Depends(get_db)):
    bank_account_type = BankAccountTypeCrud.get_bank_account_type_cruds(db, bank_account_type_id)
    if not bank_account_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),bank_account_type)

@router.post("/create-bank-account-type", status_code=201)
def post_bank_account_type(payload:BankAccountTypeSchema.MtrBankAccountTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_bank_account_type = BankAccountTypeCrud.post_bank_account_type_cruds(db, payload)
        db.add(new_bank_account_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_bank_account_type)
    return CommonResponse.payload(ResponseException(201), new_bank_account_type)

@router.delete("/delete-bank-account-type/{bank_account_type_id}", status_code=202)
def delete_bank_account_type(bank_account_type_id, db:Session=Depends(get_db)):
    erase_bank_account_type = BankAccountTypeCrud.delete_bank_account_type_cruds(db,bank_account_type_id)
    if not erase_bank_account_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_bank_account_type)

@router.put("/update-bank-account-type/{bank_account_type_id}", status_code=202)
def put_bank_account_type(payload:BankAccountTypeSchema.MtrBankAccountTypeGetSchema, bank_account_type_id,db:Session=Depends(get_db)):
    update_bank_account_type, update_data_new  = BankAccountTypeCrud.put_bank_account_type_cruds(db,payload, bank_account_type_id)
    if not update_bank_account_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-bank-account-type/{bank_account_type_id}", status_code=202)
def patch_bank_account_type(bank_account_type_id,db:Session=Depends(get_db)):
    active_bank_account_type  = BankAccountTypeCrud.patch_bank_account_type_cruds(db, bank_account_type_id)
    if not active_bank_account_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_bank_account_type.is_active = not active_bank_account_type.is_active
    db.commit()
    db.refresh(active_bank_account_type)
    return CommonResponse.payload(ResponseException(200), active_bank_account_type.is_active)