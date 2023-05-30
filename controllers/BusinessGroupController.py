from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import BusinessGroupCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import BusinessGroupSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Business Group"],prefix="/api/general")

@router.get("/get-business-groups", status_code=200)
def get_business_groups(db:Session=Depends(get_db)):
    business_groups = BusinessGroupCrud.get_business_groups_cruds(db,0,100)
    if not business_groups:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),business_groups)

@router.get("/get-business-group/{business_group_id}", status_code=200)
def get_business_group(business_group_id, db:Session=Depends(get_db)):
    business_group = BusinessGroupCrud.get_business_group_cruds(db, business_group_id)
    if not business_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),business_group)

@router.post("/create-business-group", status_code=201)
def post_business_group(payload:BusinessGroupSchema.MtrBusinessGroupGetSchema,db:Session=Depends(get_db)):
    try:
        new_business_group = BusinessGroupCrud.post_business_group_cruds(db, payload)
        db.add(new_business_group)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_business_group)
    return CommonResponse.payload(ResponseException(201), new_business_group)

@router.delete("/delete-business-group/{business_group_id}", status_code=202)
def delete_business_group(business_group_id, db:Session=Depends(get_db)):
    erase_business_group = BusinessGroupCrud.delete_business_group_cruds(db,business_group_id)
    if not erase_business_group:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_business_group)

@router.put("/update-business-group/{business_group_id}", status_code=202)
def put_business_group(payload:BusinessGroupSchema.MtrBusinessGroupGetSchema, business_group_id,db:Session=Depends(get_db)):
    update_business_group, update_data_new  = BusinessGroupCrud.put_business_group_cruds(db,payload, business_group_id)
    if not update_business_group:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-business-group/{business_group_id}", status_code=202)
def patch_business_group(business_group_id,db:Session=Depends(get_db)):
    active_business_group  = BusinessGroupCrud.patch_business_group_cruds(db, business_group_id)
    if not active_business_group:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_business_group.is_active = not active_business_group.is_active
    db.commit()
    db.refresh(active_business_group)
    return CommonResponse.payload(ResponseException(200), active_business_group.is_active)