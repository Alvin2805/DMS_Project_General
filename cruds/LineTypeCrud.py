from sqlalchemy.orm import Session
from src.entities import LineTypeEntity

def get_line_types_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(LineTypeEntity.MtrLineType).order_by(LineTypeEntity.MtrLineType.line_type_id).offset(offset).limit(limit).all()


def get_line_type_cruds(db:Session,get_id:int):
    return  db.query(LineTypeEntity.MtrLineType).filter(LineTypeEntity.MtrLineType.line_type_id==get_id).first()
    

def post_line_type_cruds(db:Session, payload:LineTypeEntity.MtrLineType):
    return LineTypeEntity.MtrLineType(**payload.dict())

def delete_line_type_cruds(db:Session,get_id:int):
    return db.query(LineTypeEntity.MtrLineType).filter(LineTypeEntity.MtrLineType.line_type_id==get_id).delete(synchronize_session=False)
    
def put_line_type_cruds(db:Session,payload:LineTypeEntity.MtrLineType, get_id:int):
    edit_line_type = db.query(LineTypeEntity.MtrLineType).filter(LineTypeEntity.MtrLineType.line_type_id==get_id)
    edit_line_type.update(payload.dict())
    messages_line_type = edit_line_type.first()
    return edit_line_type, messages_line_type

def patch_line_type_cruds(db:Session, get_id:int):
    return db.query(LineTypeEntity.MtrLineType).filter(LineTypeEntity.MtrLineType.line_type_id==get_id).first()
