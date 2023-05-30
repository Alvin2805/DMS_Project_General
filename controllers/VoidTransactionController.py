from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import VoidTransactionCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import VoidTransactionSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Void Transaction"],prefix="/api/general")

@router.get("/get-void-transactions", status_code=200)
def get_void_transactions(db:Session=Depends(get_db)):
    void_transactions = VoidTransactionCrud.get_void_transactions_cruds(db,0,100)
    if not void_transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),void_transactions)

@router.get("/get-void-transaction/{void_transaction_id}", status_code=200)
def get_void_transaction(void_transaction_id, db:Session=Depends(get_db)):
    void_transaction = VoidTransactionCrud.get_void_transaction_cruds(db, void_transaction_id)
    if not void_transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),void_transaction)

@router.post("/create-void-transaction", status_code=201)
def post_void_transaction(payload:VoidTransactionSchema.MtrVoidTransactionGetSchema,db:Session=Depends(get_db)):
    try :
        new_void_transaction = VoidTransactionCrud.post_void_transaction_cruds(db, payload)
        db.add(new_void_transaction)
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_void_transaction)
    return CommonResponse.payload(ResponseException(201), new_void_transaction)

@router.delete("/delete-void-transaction/{void_transaction_id}", status_code=202)
def delete_void_transaction(void_transaction_id, db:Session=Depends(get_db)):
    erase_void_transaction = VoidTransactionCrud.delete_void_transaction_cruds(db,void_transaction_id)
    if not erase_void_transaction:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_void_transaction)

@router.put("/update-void-transaction/{void_transaction_id}", status_code=202)
def put_void_transaction(payload:VoidTransactionSchema.MtrVoidTransactionGetSchema, void_transaction_id,db:Session=Depends(get_db)):
    update_void_transaction, update_data_new  = VoidTransactionCrud.put_void_transaction_cruds(db,payload, void_transaction_id)
    if not update_void_transaction:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-void-transaction/{void_transaction_id}", status_code=202)
def patch_void_transaction(void_transaction_id,db:Session=Depends(get_db)):
    active_void_transaction  = VoidTransactionCrud.patch_void_transaction_cruds(db, void_transaction_id)
    if not active_void_transaction:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_void_transaction.is_active = not active_void_transaction.is_active
    db.commit()
    db.refresh(active_void_transaction)
    return CommonResponse.payload(ResponseException(200), active_void_transaction.is_active)