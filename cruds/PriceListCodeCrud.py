from sqlalchemy.orm import Session
from src.entities import PriceListCodeEntity

def get_price_list_codes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(PriceListCodeEntity.MtrPriceListCode).order_by(PriceListCodeEntity.MtrPriceListCode.price_list_code_id).offset(offset).limit(limit).all()


def get_price_list_code_cruds(db:Session,get_id:int):
    return  db.query(PriceListCodeEntity.MtrPriceListCode).filter(PriceListCodeEntity.MtrPriceListCode.price_list_code_id==get_id).first()
    

def post_price_list_code_cruds(db:Session, payload:PriceListCodeEntity.MtrPriceListCode):
    return PriceListCodeEntity.MtrPriceListCode(**payload.dict())

def delete_price_list_code_cruds(db:Session,get_id:int):
    return db.query(PriceListCodeEntity.MtrPriceListCode).filter(PriceListCodeEntity.MtrPriceListCode.price_list_code_id==get_id).delete(synchronize_session=False)
    
def put_price_list_code_cruds(db:Session,payload:PriceListCodeEntity.MtrPriceListCode, get_id:int):
    edit_price_list_code = db.query(PriceListCodeEntity.MtrPriceListCode).filter(PriceListCodeEntity.MtrPriceListCode.price_list_code_id==get_id)
    edit_price_list_code.update(payload.dict())
    messages_price_list_code = edit_price_list_code.first()
    return edit_price_list_code, messages_price_list_code

def patch_price_list_code_cruds(db:Session, get_id:int):
    return db.query(PriceListCodeEntity.MtrPriceListCode).filter(PriceListCodeEntity.MtrPriceListCode.price_list_code_id==get_id).first()
