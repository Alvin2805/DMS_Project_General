from sqlalchemy.orm import Session
from src.entities import GeneralLedgerProcessEntity

def get_general_ledger_processs_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess).order_by(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess.general_ledger_process_id).offset(offset).limit(limit).all()


def get_general_ledger_process_cruds(db:Session,get_id:int):
    return  db.query(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess.general_ledger_process_id==get_id).first()
    

def post_general_ledger_process_cruds(db:Session, payload:GeneralLedgerProcessEntity.MtrGeneralLedgerProcess):
    return GeneralLedgerProcessEntity.MtrGeneralLedgerProcess(**payload.dict())

def delete_general_ledger_process_cruds(db:Session,get_id:int):
    return db.query(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess.general_ledger_process_id==get_id).delete(synchronize_session=False)
    
def put_general_ledger_process_cruds(db:Session,payload:GeneralLedgerProcessEntity.MtrGeneralLedgerProcess, get_id:int):
    edit_general_ledger_process = db.query(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess.general_ledger_process_id==get_id)
    edit_general_ledger_process.update(payload.dict())
    messages_general_ledger_process = edit_general_ledger_process.first()
    return edit_general_ledger_process, messages_general_ledger_process

def patch_general_ledger_process_cruds(db:Session, get_id:int):
    return db.query(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess).filter(GeneralLedgerProcessEntity.MtrGeneralLedgerProcess.general_ledger_process_id==get_id).first()
