from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import SourceApprovalDocumentCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import SourceApprovalDocumentSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Source Approval Document"],prefix="/api/general")

@router.get("/get-source-approval-documents", status_code=200)
def get_source_approval_documents(db:Session=Depends(get_db)):
    source_approval_documents = SourceApprovalDocumentCrud.get_source_approval_documents_cruds(db,0,100)
    if not source_approval_documents:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),source_approval_documents)

@router.get("/get-source-approval-document/{source_approval_document_id}", status_code=200)
def get_source_approval_document(source_approval_document_id, db:Session=Depends(get_db)):
    source_approval_document = SourceApprovalDocumentCrud.get_source_approval_document_cruds(db, source_approval_document_id)
    if not source_approval_document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),source_approval_document)

@router.post("/create-source-approval-document", status_code=201)
def post_source_approval_document(payload:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema,db:Session=Depends(get_db)):
    try:
        new_source_approval_document = SourceApprovalDocumentCrud.post_source_approval_document_cruds(db, payload)
        db.add(new_source_approval_document)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_source_approval_document)
    return CommonResponse.payload(ResponseException(201), new_source_approval_document)

@router.delete("/delete-source-approval-document/{source_approval_document_id}", status_code=202)
def delete_source_approval_document(source_approval_document_id, db:Session=Depends(get_db)):
    erase_source_approval_document = SourceApprovalDocumentCrud.delete_source_approval_document_cruds(db,source_approval_document_id)
    if not erase_source_approval_document:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_source_approval_document)

@router.put("/update-source-approval-document/{source_approval_document_id}", status_code=202)
def put_source_approval_document(payload:SourceApprovalDocumentSchema.MtrSourceApprovalDocumentGetSchema, source_approval_document_id,db:Session=Depends(get_db)):
    update_source_approval_document, update_data_new  = SourceApprovalDocumentCrud.put_source_approval_document_cruds(db,payload, source_approval_document_id)
    if not update_source_approval_document:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-source-approval-document/{source_approval_document_id}", status_code=202)
def patch_source_approval_document(source_approval_document_id,db:Session=Depends(get_db)):
    active_source_approval_document  = SourceApprovalDocumentCrud.patch_source_approval_document_cruds(db, source_approval_document_id)
    if not active_source_approval_document:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_source_approval_document.is_active = not active_source_approval_document.is_active
    db.commit()
    db.refresh(active_source_approval_document)
    return CommonResponse.payload(ResponseException(200), active_source_approval_document.is_active)