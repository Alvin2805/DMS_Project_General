from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import JobTitleCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import JobTitleSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["Job Title"],prefix="/api/general")

@router.get("/get-job-titles", status_code=200)
def get_job_titles(db:Session=Depends(get_db)):
    job_titles = JobTitleCrud.get_job_titles_cruds(db,0,100)
    if not job_titles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),job_titles)

@router.get("/get-job-title/{job_title_id}", status_code=200)
def get_job_title(job_title_id, db:Session=Depends(get_db)):
    job_title = JobTitleCrud.get_job_title_cruds(db, job_title_id)
    if not job_title:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),job_title)

@router.post("/create-job-title", status_code=201)
def post_job_title(payload:JobTitleSchema.MtrJobTitleGetSchema,db:Session=Depends(get_db)):
    new_job_title = JobTitleCrud.post_job_title_cruds(db, payload)
    try:
        db.add(new_job_title)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_job_title)
    return CommonResponse.payload(ResponseException(201), new_job_title)

@router.delete("/delete-job-title/{job_title_id}", status_code=202)
def delete_job_title(job_title_id, db:Session=Depends(get_db)):
    erase_job_title = JobTitleCrud.delete_job_title_cruds(db,job_title_id)
    if not erase_job_title:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_job_title)

@router.put("/update-job-title/{job_title_id}", status_code=202)
def put_job_title(payload:JobTitleSchema.MtrJobTitleGetSchema, job_title_id,db:Session=Depends(get_db)):
    update_job_title, update_data_new  = JobTitleCrud.put_job_title_cruds(db,payload, job_title_id)
    if not update_job_title:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-job-title/{job_title_id}", status_code=202)
def patch_job_title(job_title_id,db:Session=Depends(get_db)):
    active_job_title  = JobTitleCrud.patch_job_title_cruds(db, job_title_id)
    if not active_job_title:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_job_title.is_active = not active_job_title.is_active
    db.commit()
    db.refresh(active_job_title)
    return CommonResponse.payload(ResponseException(200), active_job_title.is_active)