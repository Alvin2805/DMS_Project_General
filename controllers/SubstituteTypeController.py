from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import SubstituteTypeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import SubstituteTypeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Substitute Type"],prefix="/api/general")

@router.get("/get-substitute-types", status_code=200)
def get_substitue_types(db:Session=Depends(get_db)):
    substitue_types = SubstituteTypeCrud.get_substitute_types_cruds(db,0,100)
    if not substitue_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),substitue_types)

@router.get("/get-substitute-type/{substitue_type_id}", status_code=200)
def get_substitue_type(substitue_type_id, db:Session=Depends(get_db)):
    substitue_type = SubstituteTypeCrud.get_substitute_type_cruds(db, substitue_type_id)
    if not substitue_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),substitue_type)

@router.post("/create-substitute-type", status_code=201)
def post_substitue_type(payload:SubstituteTypeSchema.MtrSubstituteTypeGetSchema,db:Session=Depends(get_db)):
    try :
        new_substitute_type = SubstituteTypeCrud.post_substitute_type_cruds(db, payload)
        db.add(new_substitute_type)
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_substitute_type)
    return CommonResponse.payload(ResponseException(201), new_substitute_type)

@router.delete("/delete-substitue-type/{substitue_type_id}", status_code=202)
def delete_substitue_type(substitue_type_id, db:Session=Depends(get_db)):
    erase_substitue_type = SubstituteTypeCrud.delete_substitue_type_cruds(db,substitue_type_id)
    if not erase_substitue_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_substitue_type)

@router.put("/update-substitute-type/{substitue_type_id}", status_code=202)
def put_substitue_type(payload:SubstituteTypeSchema.MtrSubstituteTypeGetSchema, substitue_type_id,db:Session=Depends(get_db)):
    update_substitue_type, update_data_new  = SubstituteTypeCrud.put_substitute_type_cruds(db,payload, substitue_type_id)
    if not update_substitue_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-substitute-type/{substitue_type_id}", status_code=202)
def patch_substitue_type(substitue_type_id,db:Session=Depends(get_db)):
    active_substitue_type  = SubstituteTypeCrud.patch_substitute_type_cruds(db, substitue_type_id)
    if not active_substitue_type:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_substitue_type.is_active = not active_substitue_type.is_active
    db.commit()
    db.refresh(active_substitue_type)
    return CommonResponse.payload(ResponseException(200), active_substitue_type.is_active)