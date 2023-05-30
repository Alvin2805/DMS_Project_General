from sqlalchemy.orm import Session
from src.entities import FinanceAreaEntity

def get_finance_areas_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(FinanceAreaEntity.MtrFinanceArea).order_by(FinanceAreaEntity.MtrFinanceArea.finance_area_id).offset(offset).limit(limit).all()


def get_finance_area_cruds(db:Session,get_id:int):
    return  db.query(FinanceAreaEntity.MtrFinanceArea).filter(FinanceAreaEntity.MtrFinanceArea.finance_area_id==get_id).first()
    

def post_finance_area_cruds(db:Session, payload:FinanceAreaEntity.MtrFinanceArea):
    return FinanceAreaEntity.MtrFinanceArea(**payload.dict())

def delete_finance_area_cruds(db:Session,get_id:int):
    return db.query(FinanceAreaEntity.MtrFinanceArea).filter(FinanceAreaEntity.MtrFinanceArea.finance_area_id==get_id).delete(synchronize_session=False)
    
def put_finance_area_cruds(db:Session,payload:FinanceAreaEntity.MtrFinanceArea, get_id:int):
    edit_finance_area = db.query(FinanceAreaEntity.MtrFinanceArea).filter(FinanceAreaEntity.MtrFinanceArea.finance_area_id==get_id)
    edit_finance_area.update(payload.dict())
    messages_finance_area = edit_finance_area.first()
    return edit_finance_area, messages_finance_area

def patch_finance_area_cruds(db:Session, get_id:int):
    return db.query(FinanceAreaEntity.MtrFinanceArea).filter(FinanceAreaEntity.MtrFinanceArea.finance_area_id==get_id).first()
