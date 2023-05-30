from sqlalchemy.orm import Session
from src.entities import BusinessScopeEntity

def get_business_scopes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(BusinessScopeEntity.MtrBusinessScope).order_by(BusinessScopeEntity.MtrBusinessScope.business_scope_id).offset(offset).limit(limit).all()


def get_business_scope_cruds(db:Session,get_id:int):
    return  db.query(BusinessScopeEntity.MtrBusinessScope).filter(BusinessScopeEntity.MtrBusinessScope.business_scope_id==get_id).first()
    

def post_business_scope_cruds(db:Session, payload:BusinessScopeEntity.MtrBusinessScope):
    return BusinessScopeEntity.MtrBusinessScope(**payload.dict())

def delete_business_scope_cruds(db:Session,get_id:int):
    return db.query(BusinessScopeEntity.MtrBusinessScope).filter(BusinessScopeEntity.MtrBusinessScope.business_scope_id==get_id).delete(synchronize_session=False)
    
def put_business_scope_cruds(db:Session,payload:BusinessScopeEntity.MtrBusinessScope, get_id:int):
    edit_business_scope = db.query(BusinessScopeEntity.MtrBusinessScope).filter(BusinessScopeEntity.MtrBusinessScope.business_scope_id==get_id)
    edit_business_scope.update(payload.dict())
    messages_business_scope = edit_business_scope.first()
    return edit_business_scope, messages_business_scope

def patch_business_scope_cruds(db:Session, get_id:int):
    return db.query(BusinessScopeEntity.MtrBusinessScope).filter(BusinessScopeEntity.MtrBusinessScope.business_scope_id==get_id).first()
