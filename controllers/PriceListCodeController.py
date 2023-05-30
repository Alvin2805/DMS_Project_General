from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import PriceListCodeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import PriceListCodeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Price List Code"],prefix="/api/general")

@router.get("/get-price-list-codes", status_code=200)
def get_price_list_codes(db:Session=Depends(get_db)):
    price_list_codes = PriceListCodeCrud.get_price_list_codes_cruds(db,0,100)
    if not price_list_codes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),price_list_codes)

@router.get("/get-price-list-code/{price_list_code_id}", status_code=200)
def get_price_list_code(price_list_code_id = None, db:Session=Depends(get_db)):
    price_list_code = PriceListCodeCrud.get_price_list_code_cruds(db, price_list_code_id)
    if not price_list_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),price_list_code)

@router.post("/create-price-list-code", status_code=201)
def post_price_list_code(payload:PriceListCodeSchema.MtrPriceListCodeGetSchema,db:Session=Depends(get_db)):
    try:
        new_price_list_code = PriceListCodeCrud.post_price_list_code_cruds(db, payload)
        db.add(new_price_list_code)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_price_list_code)
    return CommonResponse.payload(ResponseException(201), new_price_list_code)

@router.delete("/delete-price-list-code/{price_list_code_id}", status_code=202)
def delete_price_list_code(price_list_code_id, db:Session=Depends(get_db)):
    erase_price_list_code = PriceListCodeCrud.delete_price_list_code_cruds(db,price_list_code_id)
    if not erase_price_list_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_price_list_code)

@router.put("/update-price-list-code/{price_list_code_id}", status_code=202)
def put_price_list_code(payload:PriceListCodeSchema.MtrPriceListCodeGetSchema, price_list_code_id,db:Session=Depends(get_db)):
    update_price_list_code, update_data_new  = PriceListCodeCrud.put_price_list_code_cruds(db,payload, price_list_code_id)
    if not update_price_list_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-price-list-code/{price_list_code_id}", status_code=202)
def patch_price_list_code(price_list_code_id,db:Session=Depends(get_db)):
    active_price_list_code  = PriceListCodeCrud.patch_price_list_code_cruds(db, price_list_code_id)
    if not active_price_list_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_price_list_code.is_active = not active_price_list_code.is_active
    db.commit()
    db.refresh(active_price_list_code)
    return CommonResponse.payload(ResponseException(200), active_price_list_code.is_active)