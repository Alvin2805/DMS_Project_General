from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import GeneralLedgerDimensionTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import GeneralLedgerDimensionTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["General Ledger Dimension Type"],prefix="/api/general")

@router.get("/get-general-ledger-dimension-types", status_code=200)
def get_general_ledger_dimension_types(db:Session=Depends(get_db)):
    general_ledger_dimension_types = GeneralLedgerDimensionTypeCrud.get_general_ledger_dimension_types_cruds(db,0,100)
    if not general_ledger_dimension_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),general_ledger_dimension_types)

@router.get("/get-general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=200)
def get_general_ledger_dimension_type(general_ledger_dimension_type_id, db:Session=Depends(get_db)):
    general_ledger_dimension_type = GeneralLedgerDimensionTypeCrud.get_general_ledger_dimension_type_cruds(db, general_ledger_dimension_type_id)
    if not general_ledger_dimension_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),general_ledger_dimension_type)

@router.post("/create-general-ledger-dimension-type", status_code=201)
def post_general_ledger_dimension_type(payload:GeneralLedgerDimensionTypeSchema.MtrGeneralLedgerDimensionTypeGetSchema,db:Session=Depends(get_db)):
    try :
        new_general_ledger_dimension_type = GeneralLedgerDimensionTypeCrud.post_general_ledger_dimension_type_cruds(db, payload)
        db.add(new_general_ledger_dimension_type)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_general_ledger_dimension_type)
    return CommonResponse.payload(ResponseException(201), new_general_ledger_dimension_type)

@router.delete("/delete-general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=202)
def delete_general_ledger_dimension_type(general_ledger_dimension_type_id, db:Session=Depends(get_db)):
    erase_general_ledger_dimension_type = GeneralLedgerDimensionTypeCrud.delete_general_ledger_dimension_type_cruds(db,general_ledger_dimension_type_id)
    if not erase_general_ledger_dimension_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_general_ledger_dimension_type)

@router.put("/update-general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=202)
def put_general_ledger_dimension_type(payload:GeneralLedgerDimensionTypeSchema.MtrGeneralLedgerDimensionTypeGetSchema, general_ledger_dimension_type_id,db:Session=Depends(get_db)):
    update_general_ledger_dimension_type, update_data_new  = GeneralLedgerDimensionTypeCrud.put_general_ledger_dimension_type_cruds(db,payload, general_ledger_dimension_type_id)
    if not update_general_ledger_dimension_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-general-ledger-dimension-type/{general_ledger_dimension_type_id}", status_code=202)
def patch_general_ledger_dimension_type(general_ledger_dimension_type_id,db:Session=Depends(get_db)):
    active_general_ledger_dimension_type  = GeneralLedgerDimensionTypeCrud.patch_general_ledger_dimension_type_cruds(db, general_ledger_dimension_type_id)
    if not active_general_ledger_dimension_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_general_ledger_dimension_type.is_active = not active_general_ledger_dimension_type.is_active
    db.commit()
    db.refresh(active_general_ledger_dimension_type)
    return CommonResponse.payload(ResponseException(200), active_general_ledger_dimension_type.is_active)