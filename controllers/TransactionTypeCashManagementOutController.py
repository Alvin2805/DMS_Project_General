from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import TransactionTypeCashManagementOutCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import TransactionTypeCashManagementOutSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Transaction Type Cash Management Out"],prefix="/api/general")

@router.get("/get-transaction-type-cash-management-outs", status_code=200)
def get_transaction_type_cash_management_outs(db:Session=Depends(get_db)):
    transaction_type_cash_management_outs = TransactionTypeCashManagementOutCrud.get_transaction_type_cash_management_outs_cruds(db,0,100)
    if not transaction_type_cash_management_outs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),transaction_type_cash_management_outs)

@router.get("/get-transaction-type-cash-management-out/{transaction_type_cash_management_out_id}", status_code=200)
def get_transaction_type_cash_management_out(transaction_type_cash_management_out_id, db:Session=Depends(get_db)):
    transaction_type_cash_management_out = TransactionTypeCashManagementOutCrud.get_transaction_type_cash_management_out_cruds(db, transaction_type_cash_management_out_id)
    if not transaction_type_cash_management_out:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),transaction_type_cash_management_out)

@router.post("/create-transaction-type-cash-management-out", status_code=201)
def post_transaction_type_cash_management_out(payload:TransactionTypeCashManagementOutSchema.MtrTransactionTypeCashManagementOutGetSchema,db:Session=Depends(get_db)):
    try:
        new_transaction_type_cash_management_out = TransactionTypeCashManagementOutCrud.post_transaction_type_cash_management_out_cruds(db, payload)
        db.add(new_transaction_type_cash_management_out)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_transaction_type_cash_management_out)
    return CommonResponse.payload(ResponseException(201), new_transaction_type_cash_management_out)

@router.delete("/delete-transaction-type-cash-management-out/{transaction_type_cash_management_out_id}", status_code=202)
def delete_transaction_type_cash_management_out(transaction_type_cash_management_out_id, db:Session=Depends(get_db)):
    erase_transaction_type_cash_management_out = TransactionTypeCashManagementOutCrud.delete_transaction_type_cash_management_out_cruds(db,transaction_type_cash_management_out_id)
    if not erase_transaction_type_cash_management_out:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_transaction_type_cash_management_out)

@router.put("/update-transaction-type-cash-management-out/{transaction_type_cash_management_out_id}", status_code=202)
def put_transaction_type_cash_management_out(payload:TransactionTypeCashManagementOutSchema.MtrTransactionTypeCashManagementOutGetSchema, transaction_type_cash_management_out_id,db:Session=Depends(get_db)):
    update_transaction_type_cash_management_out, update_data_new  = TransactionTypeCashManagementOutCrud.put_transaction_type_cash_management_out_cruds(db,payload, transaction_type_cash_management_out_id)
    if not update_transaction_type_cash_management_out:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-transaction-type-cash-management-out/{transaction_type_cash_management_out_id}", status_code=202)
def patch_transaction_type_cash_management_out(transaction_type_cash_management_out_id,db:Session=Depends(get_db)):
    active_transaction_type_cash_management_out  = TransactionTypeCashManagementOutCrud.patch_transaction_type_cash_management_out_cruds(db, transaction_type_cash_management_out_id)
    if not active_transaction_type_cash_management_out:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_transaction_type_cash_management_out.is_active = not active_transaction_type_cash_management_out.is_active
    db.commit()
    db.refresh(active_transaction_type_cash_management_out)
    return CommonResponse.payload(ResponseException(200), active_transaction_type_cash_management_out.is_active)