from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import BillableToCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import BillableToSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Billable To"],prefix="/api/general")

@router.get("/get-billable-tos", status_code=200)
def get_billables_to(db:Session=Depends(get_db)):
    billables_to = BillableToCrud.get_billables_to_cruds(db,0,100)
    if not billables_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),billables_to)

@router.get("/get-billable-to/{billable_to_id}", status_code=200)
def get_billable_to(billable_to_id, db:Session=Depends(get_db)):
    billable_to = BillableToCrud.get_billable_to_cruds(db, billable_to_id)
    if not billable_to:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),billable_to)

@router.post("/create-billable-to", status_code=201)
def post_billable_to(payload:BillableToSchema.MtrBillableToGetSchema,db:Session=Depends(get_db)):
    try:
        new_billable_to = BillableToCrud.post_billable_to_cruds(db, payload)
        db.add(new_billable_to)
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_billable_to)
    return CommonResponse.payload(ResponseException(201), new_billable_to)

@router.delete("/delete-billable-to/{billable_to_id}", status_code=202)
def delete_billable_to(billable_to_id, db:Session=Depends(get_db)):
    erase_billable_to = BillableToCrud.delete_billable_to_cruds(db,billable_to_id)
    if not erase_billable_to:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_billable_to)

@router.put("/update-billable-to/{billable_to_id}", status_code=202)
def put_billable_to(payload:BillableToSchema.MtrBillableToGetSchema, billable_to_id,db:Session=Depends(get_db)):
    update_billable_to, update_data_new  = BillableToCrud.put_billable_to_cruds(db,payload, billable_to_id)
    if not update_billable_to:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-billable-to/{billable_to_id}", status_code=202)
def patch_billable_to(billable_to_id,db:Session=Depends(get_db)):
    active_billable_to  = BillableToCrud.patch_billable_to_cruds(db, billable_to_id)
    if not active_billable_to:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_billable_to.is_active = not active_billable_to.is_active
    db.commit()
    db.refresh(active_billable_to)
    return CommonResponse.payload(ResponseException(200), active_billable_to.is_active)