from sqlalchemy.orm import Session
from src.entities import GeneralLedgerAccountTypeEntity

def get_general_ledger_account_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType).order_by(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType.general_ledger_account_type_id).offset(offset).limit(limit).all()


def get_general_ledger_account_type_cruds(db:Session,get_id:int):
    return  db.query(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id).first()
    

def post_general_ledger_account_type_cruds(db:Session, payload:GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType):
    return GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType(**payload.dict())

def delete_general_ledger_account_type_cruds(db:Session,get_id:int):
    return db.query(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id).delete(synchronize_session=False)
    
def put_general_ledger_account_type_cruds(db:Session,payload:GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType, get_id:int):
    edit_general_ledger_account_type = db.query(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id)
    edit_general_ledger_account_type.update(payload.dict())
    messages_general_ledger_account_type = edit_general_ledger_account_type.first()
    return edit_general_ledger_account_type, messages_general_ledger_account_type

def patch_general_ledger_account_type_cruds(db:Session, get_id:int):
    return db.query(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType).filter(GeneralLedgerAccountTypeEntity.MtrGeneralLedgerAccountType.general_ledger_account_type_id==get_id).first()
