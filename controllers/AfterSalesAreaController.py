from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import AfterSalesAreaCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import AfterSalesAreaSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["After Sales Area"],prefix="/api/general")

@router.get("/get-after-sales-areas", status_code=200)
def get_after_sales_areas(db:Session=Depends(get_db)):
    after_sales_areass = AfterSalesAreaCrud.get_after_sales_areas_cruds(db,0,100)
    if not after_sales_areass:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),after_sales_areass)

@router.get("/get-after-sales-area/{after_sales_area_id}", status_code=200)
def get_after_sales_area(after_sales_area_id, db:Session=Depends(get_db)):
    after_sales_area = AfterSalesAreaCrud.get_after_sales_area_cruds(db, after_sales_area_id)
    if not after_sales_area:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),after_sales_area)

@router.post("/create-after-sales-area", status_code=201)
def post_after_sales_area(payload:AfterSalesAreaSchema.MtrAfterSalesAreaGetSchema,db:Session=Depends(get_db)):
    try:
        new_after_sales_area = AfterSalesAreaCrud.post_after_sales_area_cruds(db, payload)
        db.add(new_after_sales_area)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_after_sales_area)
    return CommonResponse.payload(ResponseException(201), new_after_sales_area)

@router.delete("/delete-after-sales-area/{after_sales_area_id}", status_code=202)
def delete_after_sales_area(after_sales_area_id, db:Session=Depends(get_db)):
    erase_after_sales_area = AfterSalesAreaCrud.delete_after_sales_area_cruds(db,after_sales_area_id)
    if not erase_after_sales_area:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_after_sales_area)

@router.put("/update-after-sales-area/{after_sales_area_id}", status_code=202)
def put_after_sales_area(payload:AfterSalesAreaSchema.MtrAfterSalesAreaGetSchema, after_sales_area_id,db:Session=Depends(get_db)):
    update_after_sales_area, update_data_new  = AfterSalesAreaCrud.put_after_sales_area_cruds(db,payload, after_sales_area_id)
    if not update_after_sales_area:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-after-sales-area/{after_sales_area_id}", status_code=202)
def patch_after_sales_area(after_sales_area_id,db:Session=Depends(get_db)):
    active_after_sales_area  = AfterSalesAreaCrud.patch_after_sales_area_cruds(db, after_sales_area_id)
    if not active_after_sales_area:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_after_sales_area.is_active = not active_after_sales_area.is_active
    db.commit()
    db.refresh(active_after_sales_area)
    return CommonResponse.payload(ResponseException(200), active_after_sales_area.is_active)