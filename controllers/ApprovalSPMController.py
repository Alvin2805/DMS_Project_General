from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import ApprovalSPMCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import ApprovalSPMSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Approval SPM"],prefix="/api/general")

@router.get("/get-approval-spms", status_code=200)
def get_approval_spms(db:Session=Depends(get_db)):
    approval_spmss = ApprovalSPMCrud.get_approval_spms_cruds(db,0,100)
    if not approval_spmss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),approval_spmss)

@router.get("/get-approval-spm/{approval_spm_id}", status_code=200)
def get_approval_spm(approval_spm_id, db:Session=Depends(get_db)):
    approval_spm = ApprovalSPMCrud.get_approval_spm_cruds(db, approval_spm_id)
    if not approval_spm:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),approval_spm)

@router.post("/create-approval-spm", status_code=201)
def post_approval_spm(payload:ApprovalSPMSchema.MtrApprovalSPMGetSchema,db:Session=Depends(get_db)):
    try:
        new_approval_spm = ApprovalSPMCrud.post_approval_spm_cruds(db, payload)
        db.add(new_approval_spm)
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_approval_spm)
    return CommonResponse.payload(ResponseException(201), new_approval_spm)

@router.delete("/delete-approval-spm/{approval_spm_id}", status_code=202)
def delete_approval_spm(approval_spm_id, db:Session=Depends(get_db)):
    erase_approval_spm = ApprovalSPMCrud.delete_approval_spm_cruds(db,approval_spm_id)
    if not erase_approval_spm:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_approval_spm)

@router.put("/update-approval-spm/{approval_spm_id}", status_code=202)
def put_approval_spm(payload:ApprovalSPMSchema.MtrApprovalSPMGetSchema, approval_spm_id,db:Session=Depends(get_db)):
    update_approval_spm, update_data_new  = ApprovalSPMCrud.put_approval_spm_cruds(db,payload, approval_spm_id)
    if not update_approval_spm:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-approval-spm/{approval_spm_id}", status_code=202)
def patch_approval_spm(approval_spm_id,db:Session=Depends(get_db)):
    active_approval_spm  = ApprovalSPMCrud.patch_approval_spm_cruds(db, approval_spm_id)
    if not active_approval_spm:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_approval_spm.is_active = not active_approval_spm.is_active
    db.commit()
    db.refresh(active_approval_spm)
    return CommonResponse.payload(ResponseException(200), active_approval_spm.is_active)