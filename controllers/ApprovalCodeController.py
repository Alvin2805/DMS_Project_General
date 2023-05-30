from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import ApprovalCodeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import ApprovalCodeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Approval Code"],prefix="/api/general")

@router.get("/get-approval-codes", status_code=200)
def get_approval_codes(db:Session=Depends(get_db)):
    approval_codes = ApprovalCodeCrud.get_approval_codes_cruds(db,0,100)
    if not approval_codes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),approval_codes)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
@router.get("/get-approval-code/{approval_code_id}", status_code=200)
def get_approval_code(approval_code_id, db:Session=Depends(get_db)):
    approval_code = ApprovalCodeCrud.get_approval_code_cruds(db, approval_code_id)
    if not approval_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),approval_code)

@router.post("/create-approval-code", status_code=201)
def post_approval_code(payload:ApprovalCodeSchema.MtrApprovalCodeGetSchema,db:Session=Depends(get_db)):
    try:
        new_approval_code = ApprovalCodeCrud.post_approval_code_cruds(db, payload)
        db.add(new_approval_code)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_approval_code)
    return CommonResponse.payload(ResponseException(201), new_approval_code)

@router.delete("/delete-approval-code/{approval_code_id}", status_code=202)
def delete_approval_code(approval_code_id, db:Session=Depends(get_db)):
    erase_approval_code = ApprovalCodeCrud.delete_approval_code_cruds(db,approval_code_id)
    if not erase_approval_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_approval_code)

@router.put("/update-approval-code/{approval_code_id}", status_code=202)
def put_approval_code(payload:ApprovalCodeSchema.MtrApprovalCodeGetSchema, approval_code_id,db:Session=Depends(get_db)):
    update_approval_code, update_data_new  = ApprovalCodeCrud.put_approval_code_cruds(db,payload, approval_code_id)
    if not update_approval_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-approval-code/{approval_code_id}", status_code=202)
def patch_approval_code(approval_code_id,db:Session=Depends(get_db)):
    active_approval_code  = ApprovalCodeCrud.patch_approval_code_cruds(db, approval_code_id)
    if not active_approval_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_approval_code.is_active = not active_approval_code.is_active
    db.commit()
    db.refresh(active_approval_code)
    return CommonResponse.payload(ResponseException(200), active_approval_code.is_active)
