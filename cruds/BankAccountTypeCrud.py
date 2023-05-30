from sqlalchemy.orm import Session
from src.entities import BankAccountTypeEntity

def get_bank_account_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BankAccountTypeEntity.MtrBankAccountType).order_by(BankAccountTypeEntity.MtrBankAccountType.bank_account_type_id).offset(offset).limit(limit).all()


def get_bank_account_type_cruds(db:Session,get_id:int):
    return  db.query(BankAccountTypeEntity.MtrBankAccountType).filter(BankAccountTypeEntity.MtrBankAccountType.bank_account_type_id==get_id).first()
    

def post_bank_account_type_cruds(db:Session, payload:BankAccountTypeEntity.MtrBankAccountType):
    return BankAccountTypeEntity.MtrBankAccountType(**payload.dict())

def delete_bank_account_type_cruds(db:Session,get_id:int):
    return db.query(BankAccountTypeEntity.MtrBankAccountType).filter(BankAccountTypeEntity.MtrBankAccountType.bank_account_type_id==get_id).delete(synchronize_session=False)
    
def put_bank_account_type_cruds(db:Session,payload:BankAccountTypeEntity.MtrBankAccountType, get_id:int):
    edit_bank_account_type = db.query(BankAccountTypeEntity.MtrBankAccountType).filter(BankAccountTypeEntity.MtrBankAccountType.bank_account_type_id==get_id)
    edit_bank_account_type.update(payload.dict())
    messages_bank_account_type = edit_bank_account_type.first()
    return edit_bank_account_type, messages_bank_account_type

def patch_bank_account_type_cruds(db:Session, get_id:int):
    return db.query(BankAccountTypeEntity.MtrBankAccountType).filter(BankAccountTypeEntity.MtrBankAccountType.bank_account_type_id==get_id).first()
