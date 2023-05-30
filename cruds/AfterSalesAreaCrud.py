from sqlalchemy.orm import Session
from src.entities import AfterSalesAreaEntity

def get_after_sales_areas_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(AfterSalesAreaEntity.MtrAfterSalesArea).order_by(AfterSalesAreaEntity.MtrAfterSalesArea.after_sales_area_id).offset(offset).limit(limit).all()


def get_after_sales_area_cruds(db:Session,get_id:int):
    return  db.query(AfterSalesAreaEntity.MtrAfterSalesArea).filter(AfterSalesAreaEntity.MtrAfterSalesArea.after_sales_area_id==get_id).first()
    

def post_after_sales_area_cruds(db:Session, payload:AfterSalesAreaEntity.MtrAfterSalesArea):
    return AfterSalesAreaEntity.MtrAfterSalesArea(**payload.dict())

def delete_after_sales_area_cruds(db:Session,get_id:int):
    return db.query(AfterSalesAreaEntity.MtrAfterSalesArea).filter(AfterSalesAreaEntity.MtrAfterSalesArea.after_sales_area_id==get_id).delete(synchronize_session=False)
    
def put_after_sales_area_cruds(db:Session,payload:AfterSalesAreaEntity.MtrAfterSalesArea, get_id:int):
    edit_after_sales_area = db.query(AfterSalesAreaEntity.MtrAfterSalesArea).filter(AfterSalesAreaEntity.MtrAfterSalesArea.after_sales_area_id==get_id)
    edit_after_sales_area.update(payload.dict())
    messages_after_sales_area = edit_after_sales_area.first()
    return edit_after_sales_area, messages_after_sales_area

def patch_after_sales_area_cruds(db:Session, get_id:int):
    return db.query(AfterSalesAreaEntity.MtrAfterSalesArea).filter(AfterSalesAreaEntity.MtrAfterSalesArea.after_sales_area_id==get_id).first()
