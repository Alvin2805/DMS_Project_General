from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import UnitOfMeasurementItemCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import UnitOfMeasurementItemSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Unit Of Measurement Item"],prefix="/api/general")

@router.get("/get-unit-of-measurement-items", status_code=200)
def get_unit_of_measurement_items(db:Session=Depends(get_db)):
    unit_of_measurement_items = UnitOfMeasurementItemCrud.get_unit_of_measurement_items_cruds(db,0,100)
    if not unit_of_measurement_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),unit_of_measurement_items)

@router.get("/get-unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=200)
def get_unit_of_measurement_item(unit_of_measurement_item_id, db:Session=Depends(get_db)):
    unit_of_measurement_item = UnitOfMeasurementItemCrud.get_unit_of_measurement_item_cruds(db, unit_of_measurement_item_id)
    if not unit_of_measurement_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),unit_of_measurement_item)

@router.post("/create-unit-of-measurement-item", status_code=201)
def post_unit_of_measurement_item(payload:UnitOfMeasurementItemSchema.MtrUnitOfMeasurementItemGetSchema,db:Session=Depends(get_db)):
    try:
        new_unit_of_measurement_item = UnitOfMeasurementItemCrud.post_unit_of_measurement_item_cruds(db, payload)
        db.add(new_unit_of_measurement_item)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_unit_of_measurement_item)
    return CommonResponse.payload(ResponseException(201), new_unit_of_measurement_item)

@router.delete("/delete-unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=202)
def delete_unit_of_measurement_item(unit_of_measurement_item_id, db:Session=Depends(get_db)):
    erase_unit_of_measurement_item = UnitOfMeasurementItemCrud.delete_unit_of_measurement_item_cruds(db,unit_of_measurement_item_id)
    if not erase_unit_of_measurement_item:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_unit_of_measurement_item)

@router.put("/update-unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=202)
def put_unit_of_measurement_item(payload:UnitOfMeasurementItemSchema.MtrUnitOfMeasurementItemGetSchema, unit_of_measurement_item_id,db:Session=Depends(get_db)):
    update_unit_of_measurement_item, update_data_new  = UnitOfMeasurementItemCrud.put_unit_of_measurement_item_cruds(db,payload, unit_of_measurement_item_id)
    if not update_unit_of_measurement_item:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-unit-of-measurement-item/{unit_of_measurement_item_id}", status_code=202)
def patch_unit_of_measurement_item(unit_of_measurement_item_id,db:Session=Depends(get_db)):
    active_unit_of_measurement_item  = UnitOfMeasurementItemCrud.patch_unit_of_measurement_item_cruds(db, unit_of_measurement_item_id)
    if not active_unit_of_measurement_item:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_unit_of_measurement_item.is_active = not active_unit_of_measurement_item.is_active
    db.commit()
    db.refresh(active_unit_of_measurement_item)
    return CommonResponse.payload(ResponseException(200), active_unit_of_measurement_item.is_active)