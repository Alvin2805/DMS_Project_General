from typing import List, Optional
from pydantic import BaseModel

class MtrProvinceSchema(BaseModel):
    is_active:Optional[bool]=None
    province_id:Optional[int]=None
    province_code:str
    province_name:str
    country_id:int

    class Config:
        orm_mode = True

class MtrProvinceRequest(BaseModel):
    province_code:str
    province_name:str
    country_id:int

class MtrProvinceResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrProvinceSchema]

class MtrProvinceResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrProvinceSchema
