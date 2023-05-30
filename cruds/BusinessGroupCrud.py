from sqlalchemy.orm import Session
from src.entities import BusinessGroupEntity

def get_business_groups_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BusinessGroupEntity.MtrBusinessGroup).order_by(BusinessGroupEntity.MtrBusinessGroup.business_group_id).offset(offset).limit(limit).all()


def get_business_group_cruds(db:Session,get_id:int):
    return  db.query(BusinessGroupEntity.MtrBusinessGroup).filter(BusinessGroupEntity.MtrBusinessGroup.business_group_id==get_id).first()
    

def post_business_group_cruds(db:Session, payload:BusinessGroupEntity.MtrBusinessGroup):
    return BusinessGroupEntity.MtrBusinessGroup(**payload.dict())

def delete_business_group_cruds(db:Session,get_id:int):
    return db.query(BusinessGroupEntity.MtrBusinessGroup).filter(BusinessGroupEntity.MtrBusinessGroup.business_group_id==get_id).delete(synchronize_session=False)
    
def put_business_group_cruds(db:Session,payload:BusinessGroupEntity.MtrBusinessGroup, get_id:int):
    edit_business_group = db.query(BusinessGroupEntity.MtrBusinessGroup).filter(BusinessGroupEntity.MtrBusinessGroup.business_group_id==get_id)
    edit_business_group.update(payload.dict())
    messages_business_group = edit_business_group.first()
    return edit_business_group, messages_business_group

def patch_business_group_cruds(db:Session, get_id:int):
    return db.query(BusinessGroupEntity.MtrBusinessGroup).filter(BusinessGroupEntity.MtrBusinessGroup.business_group_id==get_id).first()
