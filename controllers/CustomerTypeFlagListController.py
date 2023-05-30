from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import CustomerTypeFlagListCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import CustomerTypeFlagListSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Customer Type Flag List"],prefix="/api/general")

@router.get("/get-customer-type-flag-lists", status_code=200)
def get_customer_type_flag_lists(db:Session=Depends(get_db)):
    customer_type_flag_listss = CustomerTypeFlagListCrud.get_customer_type_flag_lists_cruds(db,0,100)
    if not customer_type_flag_listss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),customer_type_flag_listss)

@router.get("/get-customer-type-flag-list/{customer_type_flag_list_id}", status_code=200)
def get_customer_type_flag_list(customer_type_flag_list_id, db:Session=Depends(get_db)):
    customer_type_flag_list = CustomerTypeFlagListCrud.get_customer_type_flag_list_cruds(db, customer_type_flag_list_id)
    if not customer_type_flag_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),customer_type_flag_list)

@router.post("/create-customer-type-flag-list", status_code=201)
def post_customer_type_flag_list(payload:CustomerTypeFlagListSchema.MtrCustomerTypeFlagListGetSchema,db:Session=Depends(get_db)):
    try:
        new_customer_type_flag_list = CustomerTypeFlagListCrud.post_customer_type_flag_list_cruds(db, payload)
        db.add(new_customer_type_flag_list)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_customer_type_flag_list)
    return CommonResponse.payload(ResponseException(201), new_customer_type_flag_list)

@router.delete("/delete-customer-type-flag-list/{customer_type_flag_list_id}", status_code=202)
def delete_customer_type_flag_list(customer_type_flag_list_id, db:Session=Depends(get_db)):
    erase_customer_type_flag_list = CustomerTypeFlagListCrud.delete_customer_type_flag_list_cruds(db,customer_type_flag_list_id)
    if not erase_customer_type_flag_list:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_customer_type_flag_list)

@router.put("/update-customer-type-flag-list/{customer_type_flag_list_id}", status_code=202)
def put_customer_type_flag_list(payload:CustomerTypeFlagListSchema.MtrCustomerTypeFlagListGetSchema, customer_type_flag_list_id,db:Session=Depends(get_db)):
    update_customer_type_flag_list, update_data_new  = CustomerTypeFlagListCrud.put_customer_type_flag_list_cruds(db,payload, customer_type_flag_list_id)
    if not update_customer_type_flag_list:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-customer-type-flag-list/{customer_type_flag_list_id}", status_code=202)
def patch_customer_type_flag_list(customer_type_flag_list_id,db:Session=Depends(get_db)):
    active_customer_type_flag_list  = CustomerTypeFlagListCrud.patch_customer_type_flag_list_cruds(db, customer_type_flag_list_id)
    if not active_customer_type_flag_list:
        db.commit()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_customer_type_flag_list.is_active = not active_customer_type_flag_list.is_active
    db.commit()
    db.refresh(active_customer_type_flag_list)
    return CommonResponse.payload(ResponseException(200), active_customer_type_flag_list.is_active)