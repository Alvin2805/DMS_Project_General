from sqlalchemy.orm import Session
from src.entities import VatEntity

def get_vat_companies(db:Session, offset:int=0, limit:int=100):
    return db.query(VatEntity.MtrVatCompany).order_by(VatEntity.MtrVatCompany.vat_id).offset(offset).limit(limit).all()


def get_vat_company(db:Session,get_id:int):
    return  db.query(VatEntity.MtrVatCompany).filter(VatEntity.MtrVatCompany.vat_id==get_id).first()
    

def post_vat_company(db:Session, payload:VatEntity.MtrVatCompany):
    return VatEntity.MtrVatCompany(**payload.dict())

def delete_vat_company(db:Session,get_id:int):
    return db.query(VatEntity.MtrVatCompany).filter(VatEntity.MtrVatCompany.vat_id==get_id).delete(synchronize_session=False)
    
def put_vat_company(db:Session,payload:VatEntity.MtrVatCompany, get_id:int):
    update_vat = db.query(VatEntity.MtrVatCompany).filter(VatEntity.MtrVatCompany.vat_id==get_id)
    update_vat.update(payload.dict())
    message_vat_update = update_vat.first()
    return update_vat, message_vat_update

def patch_vat_company(db:Session, get_id:int):
    return db.query(VatEntity.MtrVatCompany).filter(VatEntity.MtrVatCompany.vat_id==get_id).first()
