from sqlalchemy.orm import Session
from src.entities import ApprovalCodeEntity

def get_approval_codes_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(ApprovalCodeEntity.MtrApprovalCode).order_by(ApprovalCodeEntity.MtrApprovalCode.approval_code_id).offset(offset).limit(limit).all()


def get_approval_code_cruds(db:Session,get_id:int):
    return  db.query(ApprovalCodeEntity.MtrApprovalCode).filter(ApprovalCodeEntity.MtrApprovalCode.approval_code_id==get_id).first()
    

def post_approval_code_cruds(db:Session, payload:ApprovalCodeEntity.MtrApprovalCode):
    return ApprovalCodeEntity.MtrApprovalCode(**payload.dict())

def delete_approval_code_cruds(db:Session,get_id:int):
    return db.query(ApprovalCodeEntity.MtrApprovalCode).filter(ApprovalCodeEntity.MtrApprovalCode.approval_code_id==get_id).delete(synchronize_session=False)
    
def put_approval_code_cruds(db:Session,payload:ApprovalCodeEntity.MtrApprovalCode, get_id:int):
    edit_approval_code = db.query(ApprovalCodeEntity.MtrApprovalCode).filter(ApprovalCodeEntity.MtrApprovalCode.approval_code_id==get_id)
    edit_approval_code.update(payload.dict())
    messages_approval_code = edit_approval_code.first()
    return edit_approval_code, messages_approval_code

def patch_approval_code_cruds(db:Session, get_id:int):
    return db.query(ApprovalCodeEntity.MtrApprovalCode).filter(ApprovalCodeEntity.MtrApprovalCode.approval_code_id==get_id).first()
