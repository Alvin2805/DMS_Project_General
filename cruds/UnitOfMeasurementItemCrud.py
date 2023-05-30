from sqlalchemy.orm import Session
from src.entities import UnitOfMeasurementItemEntity

def get_unit_of_measurement_items_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem).order_by(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem.unit_of_measurement_item_id).offset(offset).limit(limit).all()


def get_unit_of_measurement_item_cruds(db:Session,get_id:int):
    return  db.query(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id).first()
    

def post_unit_of_measurement_item_cruds(db:Session, payload:UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem):
    return UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem(**payload.dict())

def delete_unit_of_measurement_item_cruds(db:Session,get_id:int):
    return db.query(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id).delete(synchronize_session=False)
    
def put_unit_of_measurement_item_cruds(db:Session,payload:UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem, get_id:int):
    edit_unit_of_measurement_item = db.query(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id)
    edit_unit_of_measurement_item.update(payload.dict())
    messages_unit_of_measurement_item = edit_unit_of_measurement_item.first()
    return edit_unit_of_measurement_item, messages_unit_of_measurement_item

def patch_unit_of_measurement_item_cruds(db:Session, get_id:int):
    return db.query(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem).filter(UnitOfMeasurementItemEntity.MtrUnitOfMeasurementItem.unit_of_measurement_item_id==get_id).first()
