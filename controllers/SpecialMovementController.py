from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import SpecialMovementCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import SpecialMovementSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Special Movement"],prefix="/api/general")

@router.get("/get-special-movements", status_code=200)
def get_special_movements(db:Session=Depends(get_db)):
    special_movements = SpecialMovementCrud.get_special_movements_cruds(db,0,100)
    if not special_movements:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),special_movements)

@router.get("/get-special-movement/{special_movement_id}", status_code=200)
def get_special_movement(special_movement_id, db:Session=Depends(get_db)):
    special_movement = SpecialMovementCrud.get_special_movement_cruds(db, special_movement_id)
    if not special_movement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),special_movement)

@router.post("/create-special-movement", status_code=201)
def post_special_movement(payload:SpecialMovementSchema.MtrSpecialMovementGetSchema,db:Session=Depends(get_db)):
    try:
        new_special_movement = SpecialMovementCrud.post_special_movement_cruds(db, payload)
        db.add(new_special_movement)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_special_movement)
    return CommonResponse.payload(ResponseException(201), new_special_movement)

@router.delete("/delete-special-movement/{special_movement_id}", status_code=202)
def delete_special_movement(special_movement_id, db:Session=Depends(get_db)):
    erase_special_movement = SpecialMovementCrud.delete_special_movement_cruds(db,special_movement_id)
    if not erase_special_movement:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_special_movement)

@router.put("/update-special-movement/{special_movement_id}", status_code=202)
def put_special_movement(payload:SpecialMovementSchema.MtrSpecialMovementGetSchema, special_movement_id,db:Session=Depends(get_db)):
    update_special_movement, update_data_new  = SpecialMovementCrud.put_special_movement_cruds(db,payload, special_movement_id)
    if not update_special_movement:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-special-movement/{special_movement_id}", status_code=202)
def patch_special_movement(special_movement_id,db:Session=Depends(get_db)):
    active_special_movement  = SpecialMovementCrud.patch_special_movement_cruds(db, special_movement_id)
    if not active_special_movement:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_special_movement.is_active = not active_special_movement.is_active
    db.commit()
    db.refresh(active_special_movement)
    return CommonResponse.payload(ResponseException(200), active_special_movement.is_active)