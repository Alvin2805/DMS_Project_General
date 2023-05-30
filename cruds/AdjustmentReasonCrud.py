from sqlalchemy.orm import Session
from src.entities import AdjustmentReasonEntity

def get_adjustment_reasons_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(AdjustmentReasonEntity.MtrAdjustmentReason).order_by(AdjustmentReasonEntity.MtrAdjustmentReason.adjustment_reason_id).offset(offset).limit(limit).all()


def get_adjustment_reason_cruds(db:Session,get_id:int):
    return  db.query(AdjustmentReasonEntity.MtrAdjustmentReason).filter(AdjustmentReasonEntity.MtrAdjustmentReason.adjustment_reason_id==get_id).first()
    

def post_adjustment_reasons_cruds(db:Session, payload:AdjustmentReasonEntity.MtrAdjustmentReason):
    return AdjustmentReasonEntity.MtrAdjustmentReason(**payload.dict())

def delete_adjustment_reason_cruds(db:Session,get_id:int):
    return db.query(AdjustmentReasonEntity.MtrAdjustmentReason).filter(AdjustmentReasonEntity.MtrAdjustmentReason.adjustment_reason_id==get_id).delete(synchronize_session=False)
    
def put_adjustment_reason_cruds(db:Session,payload:AdjustmentReasonEntity.MtrAdjustmentReason, get_id:int):
    edit_adjustment_reason = db.query(AdjustmentReasonEntity.MtrAdjustmentReason).filter(AdjustmentReasonEntity.MtrAdjustmentReason.adjustment_reason_id==get_id)
    edit_adjustment_reason.update(payload.dict())
    message_adjustment_reason = edit_adjustment_reason.first()
    return edit_adjustment_reason, message_adjustment_reason

def patch_adjustment_reason_cruds(db:Session, get_id:int):
    return db.query(AdjustmentReasonEntity.MtrAdjustmentReason).filter(AdjustmentReasonEntity.MtrAdjustmentReason.adjustment_reason_id==get_id).first()
