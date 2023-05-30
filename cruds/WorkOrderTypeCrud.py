from sqlalchemy.orm import Session
from src.entities import WorkOrderTypeEntity

def get_work_order_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(WorkOrderTypeEntity.MtrWorkorderType).order_by(WorkOrderTypeEntity.MtrWorkorderType.work_order_type_id).offset(offset).limit(limit).all()


def get_work_order_type_cruds(db:Session,get_id:int):
    return  db.query(WorkOrderTypeEntity.MtrWorkorderType).filter(WorkOrderTypeEntity.MtrWorkorderType.work_order_type_id==get_id).first()
    

def post_work_order_type_cruds(db:Session, payload:WorkOrderTypeEntity.MtrWorkorderType):
    return WorkOrderTypeEntity.MtrWorkorderType(**payload.dict())

def delete_work_order_type_cruds(db:Session,get_id:int):
    return db.query(WorkOrderTypeEntity.MtrWorkorderType).filter(WorkOrderTypeEntity.MtrWorkorderType.work_order_type_id==get_id).delete(synchronize_session=False)
    
def put_work_order_type_cruds(db:Session,payload:WorkOrderTypeEntity.MtrWorkorderType, get_id:int):
    edit_work_order_type = db.query(WorkOrderTypeEntity.MtrWorkorderType).filter(WorkOrderTypeEntity.MtrWorkorderType.work_order_type_id==get_id)
    edit_work_order_type.update(payload.dict())
    messages_work_order_type = edit_work_order_type.first()
    return edit_work_order_type, messages_work_order_type

def patch_work_order_type_cruds(db:Session, get_id:int):
    return db.query(WorkOrderTypeEntity.MtrWorkorderType).filter(WorkOrderTypeEntity.MtrWorkorderType.work_order_type_id==get_id).first()
