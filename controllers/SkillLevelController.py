from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import SkillLevelCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import SkillLevelSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Skill Level"],prefix="/api/general")

@router.get("/get-skill-levels", status_code=200)
def get_skill_levels(db:Session=Depends(get_db)):
    skill_levels = SkillLevelCrud.get_skill_levels_cruds(db,0,100)
    if not skill_levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),skill_levels)

@router.get("/get-skill-level/{skill_level_id}", status_code=200)
def get_skill_level(skill_level_id, db:Session=Depends(get_db)):
    skill_level = SkillLevelCrud.get_skill_level_cruds(db, skill_level_id)
    if not skill_level:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),skill_level)

@router.post("/create-skill-level", status_code=201)
def post_skill_level(payload:SkillLevelSchema.MtrSkillLevelGetSchema,db:Session=Depends(get_db)):
    try:
        new_skill_level = SkillLevelCrud.post_skill_level_cruds(db, payload)
        db.add(new_skill_level)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_skill_level)
    return CommonResponse.payload(ResponseException(201), new_skill_level)

@router.delete("/delete-skill-level/{skill_level_id}", status_code=202)
def delete_skill_level(skill_level_id, db:Session=Depends(get_db)):
    erase_skill_level = SkillLevelCrud.delete_skill_level_cruds(db,skill_level_id)
    if not erase_skill_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_skill_level)

@router.put("/update-skill-level/{skill_level_id}", status_code=202)
def put_skill_level(payload:SkillLevelSchema.MtrSkillLevelGetSchema, skill_level_id,db:Session=Depends(get_db)):
    update_skill_level, update_data_new  = SkillLevelCrud.put_skill_level_cruds(db,payload, skill_level_id)
    if not update_skill_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-skill-level/{skill_level_id}", status_code=202)
def patch_skill_level(skill_level_id,db:Session=Depends(get_db)):
    active_skill_level  = SkillLevelCrud.patch_skill_level_cruds(db, skill_level_id)
    if not active_skill_level:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_skill_level.is_active = not active_skill_level.is_active
    db.commit()
    db.refresh(active_skill_level)
    return CommonResponse.payload(ResponseException(200), active_skill_level.is_active)