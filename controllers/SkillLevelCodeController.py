from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import SkillLevelCodeCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import SkillLevelCodeSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Skill Level Code"],prefix="/api/general")

@router.get("/get-skill-level-codes", status_code=200)
def get_skill_level_codes(db:Session=Depends(get_db)):
    skill_level_codes = SkillLevelCodeCrud.get_skill_level_codes_cruds(db,0,100)
    if not skill_level_codes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),skill_level_codes)

@router.get("/get-skill-level-code/{skill_level_code_id}", status_code=200)
def get_skill_level_code(skill_level_code_id, db:Session=Depends(get_db)):
    skill_level_code = SkillLevelCodeCrud.get_skill_level_code_cruds(db, skill_level_code_id)
    if not skill_level_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),skill_level_code)

@router.post("/create-skill-level-code", status_code=201)
def post_skill_level_code(payload:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema,db:Session=Depends(get_db)):
    try:
        new_skill_level_code = SkillLevelCodeCrud.post_skill_level_code_cruds(db, payload)
        db.add(new_skill_level_code)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_skill_level_code)
    return CommonResponse.payload(ResponseException(201), new_skill_level_code)

@router.delete("/delete-skill-level-code/{skill_level_code_id}", status_code=202)
def delete_skill_level_code(skill_level_code_id, db:Session=Depends(get_db)):
    erase_skill_level_code = SkillLevelCodeCrud.delete_skill_level_code_cruds(db,skill_level_code_id)
    if not erase_skill_level_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_skill_level_code)

@router.put("/update-skill-level-code/{skill_level_code_id}", status_code=202)
def put_skill_level_code(payload:SkillLevelCodeSchema.MtrSkillLevelCodeGetSchema, skill_level_code_id,db:Session=Depends(get_db)):
    update_skill_level_code, update_data_new  = SkillLevelCodeCrud.put_skill_level_code_cruds(db,payload, skill_level_code_id)
    if not update_skill_level_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-skill-level-code/{skill_level_code_id}", status_code=202)
def patch_skill_level_code(skill_level_code_id,db:Session=Depends(get_db)):
    active_skill_level_code  = SkillLevelCodeCrud.patch_skill_level_code_cruds(db, skill_level_code_id)
    if not active_skill_level_code:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_skill_level_code.is_active = not active_skill_level_code.is_active
    db.commit()
    db.refresh(active_skill_level_code)
    return CommonResponse.payload(ResponseException(200), active_skill_level_code.is_active)