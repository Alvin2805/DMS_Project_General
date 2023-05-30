from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from src.configs.database import get_db
from src.cruds import ProvinceCrud
from src.schemas import ProvinceSchema

router = APIRouter(tags=["Province"],prefix="/api/general")

@router.get("/province",status_code=status.HTTP_200_OK)
async def get_all_data(db:Session=Depends(get_db)):
    results = ProvinceCrud.get_province_all(db,0,100)
    if not results:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="data not found")
    return ProvinceSchema.MtrProvinceResponses(status_code=200,msg_status="success",data=results)

@router.get("/province/{id}",status_code=status.HTTP_200_OK)
async def get_by_id(id:int,db:Session=Depends(get_db)):
    result = ProvinceCrud.get_province_by_id(db,id)
    if not result:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"data with ID {id} not existed")
    return ProvinceSchema.MtrProvinceResponse(status_code=200,msg_status="success",data=result)

@router.delete("/province/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int,db:Session=Depends(get_db)):
    check = ProvinceCrud.del_province(db,id)
    if not check:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"data with ID {id} is invalid")
    return check

@router.post("/province",status_code=status.HTTP_201_CREATED)
async def create_data(request:ProvinceSchema.MtrProvinceRequest,db:Session=Depends(get_db)):
    new_data = ProvinceCrud.post_new_province(db,request)
    if not new_data:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"data already existed")
    return ProvinceSchema.MtrProvinceResponse(status_code=200,msg_status="success",data=new_data)

@router.put("/province/{id}",status_code=status.HTTP_200_OK)
async def update_data(request:ProvinceSchema.MtrProvinceRequest,id:int,db:Session=Depends(get_db)):
    update_data = ProvinceCrud.update_province(db,id,request)
    return ProvinceSchema.MtrProvinceResponse(status_code=200,msg_status="success",data=update_data)