from sqlalchemy.orm import Session
from src.entities import TaxOutTransactionEntity

def get_tax_out_transactions_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TaxOutTransactionEntity.MtrTaxOutTransaction).order_by(TaxOutTransactionEntity.MtrTaxOutTransaction.tax_out_transaction_id).offset(offset).limit(limit).all()


def get_tax_out_transaction_cruds(db:Session,get_id:int):
    return  db.query(TaxOutTransactionEntity.MtrTaxOutTransaction).filter(TaxOutTransactionEntity.MtrTaxOutTransaction.tax_out_transaction_id==get_id).first()
    

def post_tax_out_transaction_cruds(db:Session, payload:TaxOutTransactionEntity.MtrTaxOutTransaction):
    return TaxOutTransactionEntity.MtrTaxOutTransaction(**payload.dict())

def delete_tax_out_transaction_cruds(db:Session,get_id:int):
    return db.query(TaxOutTransactionEntity.MtrTaxOutTransaction).filter(TaxOutTransactionEntity.MtrTaxOutTransaction.tax_out_transaction_id==get_id).delete(synchronize_session=False)
    
def put_tax_out_transaction_cruds(db:Session,payload:TaxOutTransactionEntity.MtrTaxOutTransaction, get_id:int):
    edit_tax_out_transaction = db.query(TaxOutTransactionEntity.MtrTaxOutTransaction).filter(TaxOutTransactionEntity.MtrTaxOutTransaction.tax_out_transaction_id==get_id)
    edit_tax_out_transaction.update(payload.dict())
    messages_tax_out_transaction = edit_tax_out_transaction.first()
    return edit_tax_out_transaction, messages_tax_out_transaction

def patch_tax_out_transaction_cruds(db:Session, get_id:int):
    return db.query(TaxOutTransactionEntity.MtrTaxOutTransaction).filter(TaxOutTransactionEntity.MtrTaxOutTransaction.tax_out_transaction_id==get_id).first()
