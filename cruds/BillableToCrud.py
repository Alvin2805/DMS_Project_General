from sqlalchemy.orm import Session
from src.entities import BillableToEntity

def get_billables_to_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BillableToEntity.MtrBillableTo).order_by(BillableToEntity.MtrBillableTo.billable_to_id).offset(offset).limit(limit).all()


def get_billable_to_cruds(db:Session,get_id:int):
    return  db.query(BillableToEntity.MtrBillableTo).filter(BillableToEntity.MtrBillableTo.billable_to_id==get_id).first()
    

def post_billable_to_cruds(db:Session, payload:BillableToEntity.MtrBillableTo):
    return BillableToEntity.MtrBillableTo(**payload.dict())

def delete_billable_to_cruds(db:Session,get_id:int):
    return db.query(BillableToEntity.MtrBillableTo).filter(BillableToEntity.MtrBillableTo.billable_to_id==get_id).delete(synchronize_session=False)
    
def put_billable_to_cruds(db:Session,payload:BillableToEntity.MtrBillableTo, get_id:int):
    edit_billable_to = db.query(BillableToEntity.MtrBillableTo).filter(BillableToEntity.MtrBillableTo.billable_to_id==get_id)
    edit_billable_to.update(payload.dict())
    messages_billable_to = edit_billable_to.first()
    return edit_billable_to, messages_billable_to

def patch_billable_to_cruds(db:Session, get_id:int):
    return db.query(BillableToEntity.MtrBillableTo).filter(BillableToEntity.MtrBillableTo.billable_to_id==get_id).first()
