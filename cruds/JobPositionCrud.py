from sqlalchemy.orm import Session
from src.entities import JobPositionEntity

def get_job_positions_cruds(db:Session,offset:int=0, limit:int=100):
    return db.query(JobPositionEntity.MtrJobPosition).order_by(JobPositionEntity.MtrJobPosition.job_position_id).offset(offset).limit(limit).all()


def get_job_position_cruds(db:Session,get_id:int):
    return  db.query(JobPositionEntity.MtrJobPosition).filter(JobPositionEntity.MtrJobPosition.job_position_id==get_id).first()
    

def post_job_position_cruds(db:Session, payload:JobPositionEntity.MtrJobPosition):
    return JobPositionEntity.MtrJobPosition(**payload.dict())

def delete_job_position_cruds(db:Session,get_id:int):
    return db.query(JobPositionEntity.MtrJobPosition).filter(JobPositionEntity.MtrJobPosition.job_position_id==get_id).delete(synchronize_session=False)
    
def put_job_position_cruds(db:Session,payload:JobPositionEntity.MtrJobPosition, get_id:int):
    edit_job_position = db.query(JobPositionEntity.MtrJobPosition).filter(JobPositionEntity.MtrJobPosition.job_position_id==get_id)
    edit_job_position.update(payload.dict())
    message_job_position = edit_job_position.first()
    return edit_job_position, message_job_position

def patch_job_position_cruds(db:Session, get_id:int):
    return db.query(JobPositionEntity.MtrJobPosition).filter(JobPositionEntity.MtrJobPosition.job_position_id==get_id).first()
