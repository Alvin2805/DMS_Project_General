from sqlalchemy.orm import Session
from src.entities import TaxFormatTypeEntity

def get_tax_format_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(TaxFormatTypeEntity.MtrTaxFormatType).order_by(TaxFormatTypeEntity.MtrTaxFormatType.tax_format_type_id).offset(offset).limit(limit).all()


def get_tax_format_type_cruds(db:Session,get_id:int):
    return  db.query(TaxFormatTypeEntity.MtrTaxFormatType).filter(TaxFormatTypeEntity.MtrTaxFormatType.tax_format_type_id==get_id).first()
    

def post_tax_format_type_cruds(db:Session, payload:TaxFormatTypeEntity.MtrTaxFormatType):
    return TaxFormatTypeEntity.MtrTaxFormatType(**payload.dict())

def delete_tax_format_type_cruds(db:Session,get_id:int):
    return db.query(TaxFormatTypeEntity.MtrTaxFormatType).filter(TaxFormatTypeEntity.MtrTaxFormatType.tax_format_type_id==get_id).delete(synchronize_session=False)
    
def put_tax_format_type_cruds(db:Session,payload:TaxFormatTypeEntity.MtrTaxFormatType, get_id:int):
    edit_tax_format_type = db.query(TaxFormatTypeEntity.MtrTaxFormatType).filter(TaxFormatTypeEntity.MtrTaxFormatType.tax_format_type_id==get_id)
    edit_tax_format_type.update(payload.dict())
    messages_tax_format_type = edit_tax_format_type.first()
    return edit_tax_format_type, messages_tax_format_type

def patch_tax_format_type_cruds(db:Session, get_id:int):
    return db.query(TaxFormatTypeEntity.MtrTaxFormatType).filter(TaxFormatTypeEntity.MtrTaxFormatType.tax_format_type_id==get_id).first()
