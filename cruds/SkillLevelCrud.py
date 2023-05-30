from sqlalchemy.orm import Session
from src.entities import SkillLevelEntity

def get_skill_levels_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(SkillLevelEntity.MtrSkillLevel).order_by(SkillLevelEntity.MtrSkillLevel.skill_level_id).offset(offset).limit(limit).all()


def get_skill_level_cruds(db:Session,get_id:int):
    return  db.query(SkillLevelEntity.MtrSkillLevel).filter(SkillLevelEntity.MtrSkillLevel.skill_level_id==get_id).first()
    

def post_skill_level_cruds(db:Session, payload:SkillLevelEntity.MtrSkillLevel):
    return SkillLevelEntity.MtrSkillLevel(**payload.dict())

def delete_skill_level_cruds(db:Session,get_id:int):
    return db.query(SkillLevelEntity.MtrSkillLevel).filter(SkillLevelEntity.MtrSkillLevel.skill_level_id==get_id).delete(synchronize_session=False)
    
def put_skill_level_cruds(db:Session,payload:SkillLevelEntity.MtrSkillLevel, get_id:int):
    edit_skill_level = db.query(SkillLevelEntity.MtrSkillLevel).filter(SkillLevelEntity.MtrSkillLevel.skill_level_id==get_id)
    edit_skill_level.update(payload.dict())
    messages_skill_level = edit_skill_level.first()
    return edit_skill_level, messages_skill_level

def patch_skill_level_cruds(db:Session, get_id:int):
    return db.query(SkillLevelEntity.MtrSkillLevel).filter(SkillLevelEntity.MtrSkillLevel.skill_level_id==get_id).first()
