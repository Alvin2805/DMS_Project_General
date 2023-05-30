from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import BusinessCategoryCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import BusinessCategorySchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Business Category"],prefix="/api/general")

@router.get("/get-business-categorys", status_code=200)
def get_business_categories(db:Session=Depends(get_db)):
    business_categories = BusinessCategoryCrud.get_business_categories_cruds(db,0,100)
    if not business_categories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),business_categories)

@router.get("/get-business-category/{business_category_id}", status_code=200)
def get_business_category(business_category_id, db:Session=Depends(get_db)):
    business_category = BusinessCategoryCrud.get_business_category_cruds(db, business_category_id)
    if not business_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),business_category)

@router.post("/create-business-category", status_code=201)
def post_business_category(payload:BusinessCategorySchema.MtrBusinessCategoryGetSchema,db:Session=Depends(get_db)):
    try:
        new_business_category = BusinessCategoryCrud.post_business_category_cruds(db, payload)
        db.add(new_business_category)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_business_category)
    return CommonResponse.payload(ResponseException(201), new_business_category)

@router.delete("/delete-business-category/{business_category_id}", status_code=202)
def delete_business_category(business_category_id, db:Session=Depends(get_db)):
    erase_business_category = BusinessCategoryCrud.delete_business_category_cruds(db,business_category_id)
    if not erase_business_category:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_business_category)

@router.put("/update-business-category/{business_category_id}", status_code=202)
def put_business_category(payload:BusinessCategorySchema.MtrBusinessCategoryGetSchema, business_category_id,db:Session=Depends(get_db)):
    update_business_category, update_data_new  = BusinessCategoryCrud.put_business_category_cruds(db,payload, business_category_id)
    if not update_business_category:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-business-category/{business_category_id}", status_code=202)
def patch_business_category(business_category_id,db:Session=Depends(get_db)):
    active_business_category  = BusinessCategoryCrud.patch_business_category_cruds(db, business_category_id)
    if not active_business_category:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_business_category.is_active = not active_business_category.is_active
    db.commit()
    db.refresh(active_business_category)
    return CommonResponse.payload(ResponseException(200), active_business_category.is_active)