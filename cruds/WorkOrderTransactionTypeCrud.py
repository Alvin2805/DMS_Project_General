from sqlalchemy.orm import Session
from src.entities import WorkOrderTransactionTypeEntity

def get_work_order_transaction_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType).order_by(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType.work_order_transaction_type_id).offset(offset).limit(limit).all()


def get_work_order_transaction_type_cruds(db:Session,get_id:int):
    return  db.query(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id).first()
    

def post_work_order_transaction_type_cruds(db:Session, payload:WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType):
    return WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType(**payload.dict())

def delete_work_order_transaction_type_cruds(db:Session,get_id:int):
    return db.query(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id).delete(synchronize_session=False)
    
def put_work_order_transaction_type_cruds(db:Session,payload:WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType, get_id:int):
    edit_work_order_transaction_type = db.query(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id)
    edit_work_order_transaction_type.update(payload.dict())
    messages_work_order_transaction_type = edit_work_order_transaction_type.first()
    return edit_work_order_transaction_type, messages_work_order_transaction_type

def patch_work_order_transaction_type_cruds(db:Session, get_id:int):
    return db.query(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType).filter(WorkOrderTransactionTypeEntity.MtrWorkOrderTransactionType.work_order_transaction_type_id==get_id).first()
