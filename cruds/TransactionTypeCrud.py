from sqlalchemy.orm import Session
from src.entities import TransactionTypeEntity

def get_transaction_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TransactionTypeEntity.MtrTransactionType).order_by(TransactionTypeEntity.MtrTransactionType.transaction_type_id).offset(offset).limit(limit).all()


def get_transaction_type_cruds(db:Session,get_id:int):
    return  db.query(TransactionTypeEntity.MtrTransactionType).filter(TransactionTypeEntity.MtrTransactionType.transaction_type_id==get_id).first()
    

def post_transaction_type_cruds(db:Session, payload:TransactionTypeEntity.MtrTransactionType):
    return TransactionTypeEntity.MtrTransactionType(**payload.dict())

def delete_transaction_type_cruds(db:Session,get_id:int):
    return db.query(TransactionTypeEntity.MtrTransactionType).filter(TransactionTypeEntity.MtrTransactionType.transaction_type_id==get_id).delete(synchronize_session=False)
    
def put_transaction_type_cruds(db:Session,payload:TransactionTypeEntity.MtrTransactionType, get_id:int):
    edit_transaction_type = db.query(TransactionTypeEntity.MtrTransactionType).filter(TransactionTypeEntity.MtrTransactionType.transaction_type_id==get_id)
    edit_transaction_type.update(payload.dict())
    messages_transaction_type = edit_transaction_type.first()
    return edit_transaction_type, messages_transaction_type

def patch_transaction_type_cruds(db:Session, get_id:int):
    return db.query(TransactionTypeEntity.MtrTransactionType).filter(TransactionTypeEntity.MtrTransactionType.transaction_type_id==get_id).first()
