from typing import List, Optional
from pydantic import BaseModel


class MtrAreaSchema(BaseModel):
    is_active:Optional[bool]=None
    area_id:Optional[int]=None
    area_code:str
    description:str
    region_id:int

    class Config:
        orm_mode = True

class MtrAreaRequest(BaseModel):
    area_code:str
    description:str
    region_id:int

class MtrAreaResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrAreaSchema]

class MtrAreaResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrAreaSchema
