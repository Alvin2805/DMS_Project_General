from sqlalchemy.orm import Session
from src.entities import IncentiveLevelEntity

def get_incentive_levels_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(IncentiveLevelEntity.MtrIncentiveLevel).order_by(IncentiveLevelEntity.MtrIncentiveLevel.incentive_level_id).offset(offset).limit(limit).all()


def get_incentive_level_cruds(db:Session,get_id:int):
    return  db.query(IncentiveLevelEntity.MtrIncentiveLevel).filter(IncentiveLevelEntity.MtrIncentiveLevel.incentive_level_id==get_id).first()
    

def post_incentive_level_cruds(db:Session, payload:IncentiveLevelEntity.MtrIncentiveLevel):
    return IncentiveLevelEntity.MtrIncentiveLevel(**payload.dict())

def delete_incentive_level_cruds(db:Session,get_id:int):
    return db.query(IncentiveLevelEntity.MtrIncentiveLevel).filter(IncentiveLevelEntity.MtrIncentiveLevel.incentive_level_id==get_id).delete(synchronize_session=False)
    
def put_incentive_level_cruds(db:Session,payload:IncentiveLevelEntity.MtrIncentiveLevel, get_id:int):
    edit_incentive_level = db.query(IncentiveLevelEntity.MtrIncentiveLevel).filter(IncentiveLevelEntity.MtrIncentiveLevel.incentive_level_id==get_id)
    edit_incentive_level.update(payload.dict())
    messages_incentive_level = edit_incentive_level.first()
    return edit_incentive_level, messages_incentive_level

def patch_incentive_level_cruds(db:Session, get_id:int):
    return db.query(IncentiveLevelEntity.MtrIncentiveLevel).filter(IncentiveLevelEntity.MtrIncentiveLevel.incentive_level_id==get_id).first()
