from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import CustomerClassCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import CustomerClassSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Customer Class"],prefix="/api/general")

@router.get("/get-customer-classs", status_code=200)
def get_customer_classes(db:Session=Depends(get_db)):
    customer_classes = CustomerClassCrud.get_customer_classes_cruds(db,0,100)
    if not customer_classes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),customer_classes)

@router.get("/get-customer-class/{customer_class_id}", status_code=200)
def get_customer_class(customer_class_id, db:Session=Depends(get_db)):
    customer_class = CustomerClassCrud.get_customer_class_cruds(db, customer_class_id)
    if not customer_class:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),customer_class)

@router.post("/create-customer-class", status_code=201)
def post_customer_class(payload:CustomerClassSchema.MtrCustomerClassGetSchema,db:Session=Depends(get_db)):
    try:
        new_customer_class = CustomerClassCrud.post_customer_class_cruds(db, payload)
        db.add(new_customer_class)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_customer_class)
    return CommonResponse.payload(ResponseException(201), new_customer_class)

@router.delete("/delete-customer-class/{customer_class_id}", status_code=202)
def delete_customer_class(customer_class_id, db:Session=Depends(get_db)):
    erase_customer_class = CustomerClassCrud.delete_customer_class_cruds(db,customer_class_id)
    if not erase_customer_class:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_customer_class)

@router.put("/update-customer-class/{customer_class_id}", status_code=202)
def put_customer_class(payload:CustomerClassSchema.MtrCustomerClassGetSchema, customer_class_id,db:Session=Depends(get_db)):
    update_customer_class, update_data_new  = CustomerClassCrud.put_customer_class_cruds(db,payload, customer_class_id)
    if not update_customer_class:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-customer-class/{customer_class_id}", status_code=202)
def patch_customer_class(customer_class_id,db:Session=Depends(get_db)):
    active_customer_class  = CustomerClassCrud.patch_customer_class_cruds(db, customer_class_id)
    if not active_customer_class:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_customer_class.is_active = not active_customer_class.is_active
    db.commit()
    db.refresh(active_customer_class)
    return CommonResponse.payload(ResponseException(200), active_customer_class.is_active)