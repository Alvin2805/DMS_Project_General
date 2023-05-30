from fastapi import APIRouter,Depends,HTTPException,status
from src.payloads import CommonResponse
from src.exceptions.RequestException import ResponseException 
from src.cruds import JobPositionCrud
from src.schemas import JobPositionSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db

router = APIRouter(tags=["Job Position"],prefix="/api/general")

@router.get("/get-job-positions", status_code=status.HTTP_200_OK)
def get_job_positions(db:Session=Depends(get_db)):
    job_positions = JobPositionCrud.get_job_positions_cruds(db,0,100)
    if not job_positions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),job_positions)

@router.get("/get-job-position/{job_position_id}", status_code=status.HTTP_200_OK)
def get_job_position(job_position_id, db:Session=Depends(get_db)):
    job_position = JobPositionCrud.get_job_position_cruds(db, job_position_id)
    if not job_position:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200), job_position)

@router.post("/create-job-position", status_code=status.HTTP_201_CREATED)
def post_job_position(payload:JobPositionSchema.MtrJobPositionGetSchema,db:Session=Depends(get_db)):
    try:
        new_job_position = JobPositionCrud.post_job_position_cruds(db, payload)
        db.add(new_job_position)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_job_position)
    return CommonResponse.payload(ResponseException(201), new_job_position)

@router.delete("/delete-job-position/{job_position_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_job_position(job_position_id, db:Session=Depends(get_db)):
    erase_job_position = JobPositionCrud.delete_job_position_cruds(db,job_position_id)
    if not erase_job_position:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_job_position)

@router.put("/update-job-position/{job_position_id}", status_code=status.HTTP_202_ACCEPTED)
def put_job_position(payload:JobPositionSchema.MtrJobPositionGetSchema, job_position_id,db:Session=Depends(get_db)):
    update_job_position, update_data_new  = JobPositionCrud.put_job_position_cruds(db,payload, job_position_id)
    if not update_job_position:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-job-position/{job_position_id}", status_code=status.HTTP_202_ACCEPTED)
def patch_job_positionn(job_position_id,db:Session=Depends(get_db)):
    active_job_position  = JobPositionCrud.patch_job_position_cruds(db, job_position_id)
    if not active_job_position:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_job_position.is_active = not active_job_position.is_active
    db.commit()
    db.refresh(active_job_position)
    return CommonResponse.payload(ResponseException(200), active_job_position.is_active)