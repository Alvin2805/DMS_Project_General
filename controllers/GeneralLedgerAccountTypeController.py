from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import GeneralLedgerAccountTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import GeneralLedgerAccountTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["General Account Type"],prefix="/api/general")

@router.get("/get-general-ledger-account-types", status_code=200)
def get_general_ledger_account_types(db:Session=Depends(get_db)):
    general_ledger_account_types = GeneralLedgerAccountTypeCrud.get_general_ledger_account_types_cruds(db,0,100)
    if not general_ledger_account_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),general_ledger_account_types)

@router.get("/get-general-ledger-account-type/{general_ledger_account_type_id}", status_code=200)
def get_general_ledger_account_type(general_ledger_account_type_id, db:Session=Depends(get_db)):
    general_ledger_account_type = GeneralLedgerAccountTypeCrud.get_general_ledger_account_type_cruds(db, general_ledger_account_type_id)
    if not general_ledger_account_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),general_ledger_account_type)

@router.post("/create-general-ledger-account-type", status_code=201)
def post_general_ledger_account_type(payload:GeneralLedgerAccountTypeSchema.MtrGeneralLedgerAccountTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_general_ledger_account_type = GeneralLedgerAccountTypeCrud.post_general_ledger_account_type_cruds(db, payload)
        db.add(new_general_ledger_account_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_general_ledger_account_type)
    return CommonResponse.payload(ResponseException(201), new_general_ledger_account_type)

@router.delete("/delete-general-ledger-account-type/{general_ledger_account_type_id}", status_code=202)
def delete_general_ledger_account_type(general_ledger_account_type_id, db:Session=Depends(get_db)):
    erase_general_ledger_account_type = GeneralLedgerAccountTypeCrud.delete_general_ledger_account_type_cruds(db,general_ledger_account_type_id)
    if not erase_general_ledger_account_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_general_ledger_account_type)

@router.put("/update-general-ledger-account-type/{general_ledger_account_type_id}", status_code=202)
def put_general_ledger_account_type(payload:GeneralLedgerAccountTypeSchema.MtrGeneralLedgerAccountTypeGetSchema, general_ledger_account_type_id,db:Session=Depends(get_db)):
    update_general_ledger_account_type, update_data_new  = GeneralLedgerAccountTypeCrud.put_general_ledger_account_type_cruds(db,payload, general_ledger_account_type_id)
    if not update_general_ledger_account_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-general-ledger-account-type/{general_ledger_account_type_id}", status_code=202)
def patch_general_ledger_account_type(general_ledger_account_type_id,db:Session=Depends(get_db)):
    active_general_ledger_account_type  = GeneralLedgerAccountTypeCrud.patch_general_ledger_account_type_cruds(db, general_ledger_account_type_id)
    if not active_general_ledger_account_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_general_ledger_account_type.is_active = not active_general_ledger_account_type.is_active
    db.commit()
    db.refresh(active_general_ledger_account_type)
    return CommonResponse.payload(ResponseException(200), active_general_ledger_account_type.is_active)