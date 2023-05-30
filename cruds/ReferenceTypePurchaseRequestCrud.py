from sqlalchemy.orm import Session
from src.entities import ReferenceTypePurchaseRequestEntity

def get_reference_type_purchase_requests_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest).order_by(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest.reference_type_purchase_request_id).offset(offset).limit(limit).all()


def get_reference_type_purchase_request_cruds(db:Session,get_id:int):
    return  db.query(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest).filter(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest.reference_type_purchase_request_id==get_id).first()
    

def post_reference_type_purchase_request_cruds(db:Session, payload:ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest):
    return ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest(**payload.dict())

def delete_reference_type_purchase_request_cruds(db:Session,get_id:int):
    return db.query(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest).filter(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest.reference_type_purchase_request_id==get_id).delete(synchronize_session=False)
    
def put_reference_type_purchase_request_cruds(db:Session,payload:ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest, get_id:int):
    edit_reference_type_purchase_request = db.query(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest).filter(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest.reference_type_purchase_request_id==get_id)
    edit_reference_type_purchase_request.update(payload.dict())
    messages_reference_type_purchase_request = edit_reference_type_purchase_request.first()
    return edit_reference_type_purchase_request, messages_reference_type_purchase_request

def patch_reference_type_purchase_request_cruds(db:Session, get_id:int):
    return db.query(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest).filter(ReferenceTypePurchaseRequestEntity.MtrReferenceTypePurchaseRequest.reference_type_purchase_request_id==get_id).first()
