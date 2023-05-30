from fastapi import APIRouter,Depends,HTTPException,status
from src.payloads import CommonResponse
from src.exceptions.RequestException import ResponseException 
from src.cruds import AddressCrud
from src.schemas import AddressSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db

router = APIRouter(tags=["Address"],prefix="/api/general")

@router.get("/address", status_code=200)
def get_data(db:Session=Depends(get_db)):
    results = AddressCrud.get_addresses(db,0,100)
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),results)

@router.get("/address/{address_id}", status_code=status.HTTP_200_OK)
def get_data_id(address_id:int, db:Session=Depends(get_db)):
    result = AddressCrud.get_address_by_id(db, address_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200), result)

@router.post("/address", status_code=201)
def post_data(payload:AddressSchema.MtrAddressRequest,db:Session=Depends(get_db)):
    try :
        new_address = AddressCrud.post_address(db, payload)
        db.add(new_address)
        db.commit()
    except IntegrityError: 
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_address)
    return CommonResponse.payload(ResponseException(201), new_address)

@router.delete("/address/{address_id}", status_code=202)
def delete_data(address_id:int, db:Session=Depends(get_db)):
    delete_data = AddressCrud.delete_address(db,address_id)
    if not delete_data:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), delete_data)

@router.put("/address/{address_id}", status_code=202)
def put_data(payload:AddressSchema.MtrAddressRequest, address_id:int,db:Session=Depends(get_db)):
    update_address, update_data_new  = AddressCrud.put(db,payload, address_id)
    if not update_address:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/address/{address_id}", status_code=202)
def delete_data(address_id:int,db:Session=Depends(get_db)):
    patch_data  = AddressCrud.patch_address(db, address_id)
    if not patch_data:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    patch_data.is_active = not patch_data.is_active
    db.commit()
    db.refresh(patch_data)
    return CommonResponse.payload(ResponseException(200), patch_data.is_active)
