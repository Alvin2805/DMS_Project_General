from fastapi import APIRouter,Depends,HTTPException,status
from src.payloads import CommonResponse
from src.exceptions.RequestException import ResponseException 
from src.cruds import AdjustmentReasonCrud
from src.schemas import AdjustmentReasonSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db

router = APIRouter(tags=["Adjustment Reason"],prefix="/api/general")

@router.get("/get-adjustment-reasons", status_code=200)
def get_adjustment_reasons(db:Session=Depends(get_db)):
    adjustment_reasons = AdjustmentReasonCrud.get_adjustment_reasons_cruds(db,0,100)
    if not adjustment_reasons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),adjustment_reasons)

@router.get("/get-adjustment-reason/{adjustment_reason_id}", status_code=status.HTTP_200_OK)
def get_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    adjustment_reason = AdjustmentReasonCrud.get_adjustment_reason_cruds(db, adjustment_reason_id)
    if not adjustment_reason:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200), adjustment_reason)

@router.post("/create-adjustment-reason", status_code=201)
def post_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema,db:Session=Depends(get_db)):
    try :
        new_adjustment_reason = AdjustmentReasonCrud.post_adjustment_reasons_cruds(db, payload)
        db.add(new_adjustment_reason)
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_adjustment_reason)
    return CommonResponse.payload(ResponseException(201), new_adjustment_reason)

@router.delete("/delete-adjustment-reason/{adjustment_reason_id}", status_code=202)
def delete_adjustment_reason(adjustment_reason_id, db:Session=Depends(get_db)):
    erase_adjustment_reason = AdjustmentReasonCrud.delete_adjustment_reason_cruds(db,adjustment_reason_id)
    if not erase_adjustment_reason:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_adjustment_reason)

@router.put("/update-adjustment-reason/{adjustment_reason_id}", status_code=202)
def put_adjustment_reason(payload:AdjustmentReasonSchema.MtrAdjustmentReasonGetSchema, adjustment_reason_id,db:Session=Depends(get_db)):
    update_adjustment_reason, update_data_new  = AdjustmentReasonCrud.put_adjustment_reason_cruds(db,payload, adjustment_reason_id)
    if not update_adjustment_reason:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-adjustment-reason/{adjustment_reason_id}", status_code=202)
def patch_adjustment_reason(adjustment_reason_id,db:Session=Depends(get_db)):
    active_adjustment_reason  = AdjustmentReasonCrud.patch_adjustment_reason_cruds(db, adjustment_reason_id)
    if not active_adjustment_reason:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_adjustment_reason.is_active = not active_adjustment_reason.is_active
    db.commit()
    db.refresh(active_adjustment_reason)
    return CommonResponse.payload(ResponseException(200), active_adjustment_reason.is_active)
