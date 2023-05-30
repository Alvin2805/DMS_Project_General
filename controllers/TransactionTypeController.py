from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import TransactionTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import TransactionTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Transaction Type"],prefix="/api/general")

@router.get("/get-transaction-types", status_code=200)
def get_transaction_types(db:Session=Depends(get_db)):
    transaction_types = TransactionTypeCrud.get_transaction_types_cruds(db,0,100)
    if not transaction_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),transaction_types)

@router.get("/get-transaction-type/{transaction_type_id}", status_code=200)
def get_transaction_type(transaction_type_id, db:Session=Depends(get_db)):
    transaction_type = TransactionTypeCrud.get_transaction_type_cruds(db, transaction_type_id)
    if not transaction_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),transaction_type)

@router.post("/create-transaction-type", status_code=201)
def post_transaction_type(payload:TransactionTypeSchema.MtrTransactionTypeGetSchema,db:Session=Depends(get_db)):
    try:
        new_transaction_type = TransactionTypeCrud.post_transaction_type_cruds(db, payload)
        db.add(new_transaction_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_transaction_type)
    return CommonResponse.payload(ResponseException(201), new_transaction_type)

@router.delete("/delete-transaction-type/{transaction_type_id}", status_code=202)
def delete_transaction_type(transaction_type_id, db:Session=Depends(get_db)):
    erase_transaction_type = TransactionTypeCrud.delete_transaction_type_cruds(db,transaction_type_id)
    if not erase_transaction_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_transaction_type)

@router.put("/update-transaction-type/{transaction_type_id}", status_code=202)
def put_transaction_type(payload:TransactionTypeSchema.MtrTransactionTypeGetSchema, transaction_type_id,db:Session=Depends(get_db)):
    update_transaction_type, update_data_new  = TransactionTypeCrud.put_transaction_type_cruds(db,payload, transaction_type_id)
    if not update_transaction_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-transaction-type/{transaction_type_id}", status_code=202)
def patch_transaction_type(transaction_type_id,db:Session=Depends(get_db)):
    active_transaction_type  = TransactionTypeCrud.patch_transaction_type_cruds(db, transaction_type_id)
    if not active_transaction_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_transaction_type.is_active = not active_transaction_type.is_active
    db.commit()
    db.refresh(active_transaction_type)
    return CommonResponse.payload(ResponseException(200), active_transaction_type.is_active)