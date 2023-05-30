from sqlalchemy.orm import Session
from src.entities import JobTitleEntity

def get_job_titles_cruds(db:Session, offset:int=0, limit:int=100):
    return db.query(JobTitleEntity.MtrJobTitle).order_by(JobTitleEntity.MtrJobTitle.job_title_id).offset(offset).limit(limit).all()


def get_job_title_cruds(db:Session,get_id:int):
    return  db.query(JobTitleEntity.MtrJobTitle).filter(JobTitleEntity.MtrJobTitle.job_title_id==get_id).first()
    

def post_job_title_cruds(db:Session, payload:JobTitleEntity.MtrJobTitle):
    return JobTitleEntity.MtrJobTitle(**payload.dict())

def delete_job_title_cruds(db:Session,get_id:int):
    return db.query(JobTitleEntity.MtrJobTitle).filter(JobTitleEntity.MtrJobTitle.job_title_id==get_id).delete(synchronize_session=False)
    
def put_job_title_cruds(db:Session,payload:JobTitleEntity.MtrJobTitle, get_id:int):
    edit_job_title = db.query(JobTitleEntity.MtrJobTitle).filter(JobTitleEntity.MtrJobTitle.job_title_id==get_id)
    edit_job_title.update(payload.dict())
    messages_job_title = edit_job_title.first()
    return edit_job_title, messages_job_title

def patch_job_title_cruds(db:Session, get_id:int):
    return db.query(JobTitleEntity.MtrJobTitle).filter(JobTitleEntity.MtrJobTitle.job_title_id==get_id).first()
