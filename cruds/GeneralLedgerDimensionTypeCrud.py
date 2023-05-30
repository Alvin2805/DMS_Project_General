from sqlalchemy.orm import Session
from src.entities import GeneralLedgerDimensionTypeEntity

def get_general_ledger_dimension_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType).order_by(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType.general_ledger_dimension_type_id).offset(offset).limit(limit).all()


def get_general_ledger_dimension_type_cruds(db:Session,get_id:int):
    return  db.query(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType).filter(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType.general_ledger_dimension_type_id==get_id).first()
    

def post_general_ledger_dimension_type_cruds(db:Session, payload:GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType):
    return GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType(**payload.dict())

def delete_general_ledger_dimension_type_cruds(db:Session,get_id:int):
    return db.query(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType).filter(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType.general_ledger_dimension_type_id==get_id).delete(synchronize_session=False)
    
def put_general_ledger_dimension_type_cruds(db:Session,payload:GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType, get_id:int):
    edit_general_ledger_dimension_type = db.query(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType).filter(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType.general_ledger_dimension_type_id==get_id)
    edit_general_ledger_dimension_type.update(payload.dict())
    messages_general_ledger_dimension_type = edit_general_ledger_dimension_type.first()
    return edit_general_ledger_dimension_type, messages_general_ledger_dimension_type

def patch_general_ledger_dimension_type_cruds(db:Session, get_id:int):
    return db.query(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType).filter(GeneralLedgerDimensionTypeEntity.MtrGeneralLedgerDimensionType.general_ledger_dimension_type_id==get_id).first()
