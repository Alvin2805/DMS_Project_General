from sqlalchemy.orm import Session
from src.entities import TransactionTypeCashManagementOutEntity

def get_transaction_type_cash_management_outs_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut).order_by(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id).offset(offset).limit(limit).all()


def get_transaction_type_cash_management_out_cruds(db:Session,get_id:int):
    return  db.query(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id).first()
    

def post_transaction_type_cash_management_out_cruds(db:Session, payload:TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut):
    return TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut(**payload.dict())

def delete_transaction_type_cash_management_out_cruds(db:Session,get_id:int):
    return db.query(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id).delete(synchronize_session=False)
    
def put_transaction_type_cash_management_out_cruds(db:Session,payload:TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut, get_id:int):
    edit_transaction_type_cash_management_out = db.query(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id)
    edit_transaction_type_cash_management_out.update(payload.dict())
    messages_transaction_type_cash_management_out = edit_transaction_type_cash_management_out.first()
    return edit_transaction_type_cash_management_out, messages_transaction_type_cash_management_out

def patch_transaction_type_cash_management_out_cruds(db:Session, get_id:int):
    return db.query(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut).filter(TransactionTypeCashManagementOutEntity.MtrTransactionTypeCashManagementOut.transaction_type_cash_management_out_id==get_id).first()