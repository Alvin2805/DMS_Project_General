from sqlalchemy.orm import Session
from src.entities import AddressEntity

def get_addresses(db:Session,offset:int=0, limit:int=100):
    return db.query(AddressEntity.MtrAddress).order_by(AddressEntity.MtrAddress.address_id).offset(offset).limit(limit).all()

def get_address_by_id(db:Session,get_id:int):
    return  db.query(AddressEntity.MtrAddress).filter(AddressEntity.MtrAddress.address_id==get_id).first()

def post_address(db:Session, payload:AddressEntity.MtrAddress):
    return AddressEntity.MtrAddress(**payload.dict())

def delete_address(db:Session,get_id:int):
    return db.query(AddressEntity.MtrAddress).filter(AddressEntity.MtrAddress.address_id==get_id).delete(synchronize_session=False)
    
def put_address(db:Session,payload:AddressEntity.MtrAddress, get_id:int):
    edit_adjustment_reason = db.query(AddressEntity.MtrAddress).filter(AddressEntity.MtrAddress.address_id==get_id)
    edit_adjustment_reason.update(payload.dict())
    message_adjustment_reason = edit_adjustment_reason.first()
    return edit_adjustment_reason, message_adjustment_reason

def patch_address(db:Session, get_id:int):
    return db.query(AddressEntity.MtrAddress).filter(AddressEntity.MtrAddress.address_id==get_id).first()
