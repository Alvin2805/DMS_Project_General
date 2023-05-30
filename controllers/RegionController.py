from fastapi import APIRouter,Depends,HTTPException,status,Query
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.cruds import RegionCrud
from src.schemas import RegionSchema
from src.payloads import Pagination
from typing import Optional

router = APIRouter(tags=["Region"],prefix="/api/general")

@router.get("/region",status_code=status.HTTP_200_OK)
async def get_all_data(query:list[str]|None=Query(None),query_params:list[str]|None = Query(None),page:Optional[int]=None,page_limit:Optional[int]=None,db:Session=Depends(get_db)):
    page,limit,total_rows,total_pages,results = RegionCrud.get_region_all(db,page,page_limit,query,query_params)
    if not results:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return RegionSchema.MtrRegionPagination(status_code=200,msg_status="success",data=Pagination.PaginationSchema(
        page_limit=limit,
        page=page,
        total_rows=total_rows,
        total_pages=total_pages,
        rows=results
    ))

@router.get("/region/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int,db:Session=Depends(get_db)):
    result = RegionCrud.get_region_by_id(db,id)
    if not result:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"data with ID {id} not existed")
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=result)

@router.get("/region_params")
async def get_by_params(param:str,db:Session=Depends(get_db)):
    results = RegionCrud.get_region_by_params(db,param)
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return RegionSchema.MtrRegionResponses(status_code=200,msg_status="success",data=results)
    
@router.delete("/region/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int,db:Session=Depends(get_db)):
    check = RegionCrud.del_region(db,id)
    if not check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data with ID {id} is invalid")
    return check

@router.post("/region",status_code=status.HTTP_201_CREATED)
async def create_data(request:RegionSchema.MtrRegionRequest,db:Session=Depends(get_db)):
    new_data = RegionCrud.post_new_region(db,request)
    if not new_data:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"data already existed")
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=new_data)

@router.put("/region/{id}",status_code=status.HTTP_200_OK)
async def update_data(request:RegionSchema.MtrRegionRequest,id:int,db:Session=Depends(get_db)):
    update_data = RegionCrud.update_region(db,id,request)
    return RegionSchema.MtrRegionResponse(status_code=200,msg_status="success",data=update_data)

@router.get("/region/test", status_code=status.HTTP_200_OK)
async def get_all_data(session: Session = Depends(get_db)):
    
    results = RegionCrud.get_all_users(session)
    return results
