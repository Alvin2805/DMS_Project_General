from sqlalchemy.orm import Session
from src.entities import ApprovalSPMEntity

def get_approval_spms_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(ApprovalSPMEntity.MtrApprovalSpm).order_by(ApprovalSPMEntity.MtrApprovalSpm.approval_spm_id).offset(offset).limit(limit).all()


def get_approval_spm_cruds(db:Session,get_id:int):
    return  db.query(ApprovalSPMEntity.MtrApprovalSpm).filter(ApprovalSPMEntity.MtrApprovalSpm.approval_spm_id==get_id).first()
    

def post_approval_spm_cruds(db:Session, payload:ApprovalSPMEntity.MtrApprovalSpm):
    return ApprovalSPMEntity.MtrApprovalSpm(**payload.dict())

def delete_approval_spm_cruds(db:Session,get_id:int):
    return db.query(ApprovalSPMEntity.MtrApprovalSpm).filter(ApprovalSPMEntity.MtrApprovalSpm.approval_spm_id==get_id).delete(synchronize_session=False)
    
def put_approval_spm_cruds(db:Session,payload:ApprovalSPMEntity.MtrApprovalSpm, get_id:int):
    edit_approval_spm = db.query(ApprovalSPMEntity.MtrApprovalSpm).filter(ApprovalSPMEntity.MtrApprovalSpm.approval_spm_id==get_id)
    edit_approval_spm.update(payload.dict())
    messages_approval_spm = edit_approval_spm.first()
    return edit_approval_spm, messages_approval_spm

def patch_approval_spm_cruds(db:Session, get_id:int):
    return db.query(ApprovalSPMEntity.MtrApprovalSpm).filter(ApprovalSPMEntity.MtrApprovalSpm.approval_spm_id==get_id).first()
