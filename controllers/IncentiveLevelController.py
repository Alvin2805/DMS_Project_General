from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import IncentiveLevelCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import IncentiveLevelSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Incentive Level"],prefix="/api/general")

@router.get("/get-incentive-levels", status_code=200)
def get_incentive_levels(db:Session=Depends(get_db)):
    incentive_levels = IncentiveLevelCrud.get_incentive_levels_cruds(db,0,100)
    if not incentive_levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),incentive_levels)

@router.get("/get-incentive-level/{incentive_level_id}", status_code=200)
def get_incentive_level(incentive_level_id, db:Session=Depends(get_db)):
    incentive_level = IncentiveLevelCrud.get_incentive_level_cruds(db, incentive_level_id)
    if not incentive_level:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),incentive_level)

@router.post("/create-incentive-level", status_code=201)
def post_incentive_level(payload:IncentiveLevelSchema.MtrIncentiveLevelGetSchema,db:Session=Depends(get_db)):
    try:
        new_incentive_level = IncentiveLevelCrud.post_incentive_level_cruds(db, payload)
        db.add(new_incentive_level)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_incentive_level)
    return CommonResponse.payload(ResponseException(201), new_incentive_level)

@router.delete("/delete-incentive-level/{incentive_level_id}", status_code=202)
def delete_incentive_level(incentive_level_id, db:Session=Depends(get_db)):
    erase_incentive_level = IncentiveLevelCrud.delete_incentive_level_cruds(db,incentive_level_id)
    if not erase_incentive_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_incentive_level)

@router.put("/update-incentive-level/{incentive_level_id}", status_code=202)
def put_incentive_level(payload:IncentiveLevelSchema.MtrIncentiveLevelGetSchema, incentive_level_id,db:Session=Depends(get_db)):
    update_incentive_level, update_data_new  = IncentiveLevelCrud.put_incentive_level_cruds(db,payload, incentive_level_id)
    if not update_incentive_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-incentive-level/{incentive_level_id}", status_code=202)
def patch_incentive_level(incentive_level_id,db:Session=Depends(get_db)):
    active_incentive_level  = IncentiveLevelCrud.patch_incentive_level_cruds(db, incentive_level_id)
    if not active_incentive_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_incentive_level.is_active = not active_incentive_level.is_active
    db.commit()
    db.refresh(active_incentive_level)
    return CommonResponse.payload(ResponseException(200), active_incentive_level.is_active)