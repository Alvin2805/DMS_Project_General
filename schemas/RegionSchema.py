from typing import List, Optional
from pydantic import BaseModel
from src.payloads import Pagination

class MtrRegionSchema(BaseModel):
    is_active:Optional[bool]=None
    region_id:Optional[int]=None
    region_code:str
    region_name:str
    user_id:int

    class Config:
        orm_mode = True

class MtrRegionRequest(BaseModel):
    region_code:str
    region_name:str
    user_id:int

class MtrRegionResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrRegionSchema]

class MtrRegionResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrRegionSchema

class MtrRegionPagination(BaseModel):
    status_code:int
    msg_status:str
    data:Pagination.PaginationSchema