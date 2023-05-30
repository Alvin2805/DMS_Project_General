from fastapi import APIRouter,Depends,HTTPException,status
from src.cruds import GeneralLedgerProcessCrud
from src.exceptions.RequestException import ResponseException
from src.schemas import GeneralLedgerProcessSchema
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.configs.database import get_db
from src.payloads import CommonResponse

router = APIRouter(tags=["General Ledger Process"],prefix="/api/general")

@router.get("/get-general-ledger-processs", status_code=200)
def get_general_ledger_processs(db:Session=Depends(get_db)):
    general_ledger_processs = GeneralLedgerProcessCrud.get_general_ledger_processs_cruds(db,0,100)
    if not general_ledger_processs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payloads(ResponseException(200),general_ledger_processs)

@router.get("/get-general-ledger-process/{general_ledger_process_id}", status_code=200)
def get_general_ledger_process(general_ledger_process_id, db:Session=Depends(get_db)):
    general_ledger_process = GeneralLedgerProcessCrud.get_general_ledger_process_cruds(db, general_ledger_process_id)
    if not general_ledger_process:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    return CommonResponse.payload(ResponseException(200),general_ledger_process)

@router.post("/create-general-ledger-process", status_code=201)
def post_general_ledger_process(payload:GeneralLedgerProcessSchema.MtrGeneralLedgerProcessGetSchema,db:Session=Depends(get_db)):
    try:
        new_general_ledger_process = GeneralLedgerProcessCrud.post_general_ledger_process_cruds(db, payload)
        db.add(new_general_ledger_process)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=ResponseException(409))
    db.refresh(new_general_ledger_process)
    return CommonResponse.payload(ResponseException(201), new_general_ledger_process)

@router.delete("/delete-general-ledger-process/{general_ledger_process_id}", status_code=202)
def delete_general_ledger_process(general_ledger_process_id, db:Session=Depends(get_db)):
    erase_general_ledger_process = GeneralLedgerProcessCrud.delete_general_ledger_process_cruds(db,general_ledger_process_id)
    if not erase_general_ledger_process:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    return CommonResponse.payload(ResponseException(202), erase_general_ledger_process)

@router.put("/update-general-ledger-process/{general_ledger_process_id}", status_code=202)
def put_general_ledger_process(payload:GeneralLedgerProcessSchema.MtrGeneralLedgerProcessGetSchema, general_ledger_process_id,db:Session=Depends(get_db)):
    update_general_ledger_process, update_data_new  = GeneralLedgerProcessCrud.put_general_ledger_process_cruds(db,payload, general_ledger_process_id)
    if not update_general_ledger_process:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    db.commit()
    db.refresh(update_data_new)
    return CommonResponse.payload(ResponseException(200), update_data_new)

@router.patch("/active-general-ledger-process/{general_ledger_process_id}", status_code=202)
def patch_general_ledger_process(general_ledger_process_id,db:Session=Depends(get_db)):
    active_general_ledger_process  = GeneralLedgerProcessCrud.patch_general_ledger_process_cruds(db, general_ledger_process_id)
    if not active_general_ledger_process:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=ResponseException(404))
    active_general_ledger_process.is_active = not active_general_ledger_process.is_active
    db.commit()
    db.refresh(active_general_ledger_process)
    return CommonResponse.payload(ResponseException(200), active_general_ledger_process.is_active)