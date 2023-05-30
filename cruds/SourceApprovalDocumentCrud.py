from sqlalchemy.orm import Session
from src.entities import SourceApprovalDocumentEntity

def get_source_approval_documents_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).order_by(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id).offset(offset).limit(limit).all()


def get_source_approval_document_cruds(db:Session,get_id:int):
    return  db.query(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).filter(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==get_id).first()
    

def post_source_approval_document_cruds(db:Session, payload:SourceApprovalDocumentEntity.MtrSourceApprovalDocument):
    return SourceApprovalDocumentEntity.MtrSourceApprovalDocument(**payload.dict())

def delete_source_approval_document_cruds(db:Session,get_id:int):
    return db.query(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).filter(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==get_id).delete(synchronize_session=False)
    
def put_source_approval_document_cruds(db:Session,payload:SourceApprovalDocumentEntity.MtrSourceApprovalDocument, get_id:int):
    edit_source_approval_document = db.query(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).filter(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==get_id)
    edit_source_approval_document.update(payload.dict())
    messages_source_approval_document = edit_source_approval_document.first()
    return edit_source_approval_document, messages_source_approval_document

def patch_source_approval_document_cruds(db:Session, get_id:int):
    return db.query(SourceApprovalDocumentEntity.MtrSourceApprovalDocument).filter(SourceApprovalDocumentEntity.MtrSourceApprovalDocument.source_approval_document_id==get_id).first()
