from sqlalchemy.orm import Session
from src.entities import ItemGroupEntity

def get_item_groups_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(ItemGroupEntity.MtrItemGroup).order_by(ItemGroupEntity.MtrItemGroup.item_group_id).offset(offset).limit(limit).all()


def get_item_group_cruds(db:Session,get_id:int):
    return  db.query(ItemGroupEntity.MtrItemGroup).filter(ItemGroupEntity.MtrItemGroup.item_group_id==get_id).first()
    

def post_item_group_cruds(db:Session, payload:ItemGroupEntity.MtrItemGroup):
    return ItemGroupEntity.MtrItemGroup(**payload.dict())

def delete_item_group_cruds(db:Session,get_id:int):
    return db.query(ItemGroupEntity.MtrItemGroup).filter(ItemGroupEntity.MtrItemGroup.item_group_id==get_id).delete(synchronize_session=False)
    
def put_item_group_cruds(db:Session,payload:ItemGroupEntity.MtrItemGroup, get_id:int):
    edit_item_group = db.query(ItemGroupEntity.MtrItemGroup).filter(ItemGroupEntity.MtrItemGroup.item_group_id==get_id)
    edit_item_group.update(payload.dict())
    messages_item_group = edit_item_group.first()
    return edit_item_group, messages_item_group

def patch_item_group_cruds(db:Session, get_id:int):
    return db.query(ItemGroupEntity.MtrItemGroup).filter(ItemGroupEntity.MtrItemGroup.item_group_id==get_id).first()
