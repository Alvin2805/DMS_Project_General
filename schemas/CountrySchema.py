from typing import List,Optional
from pydantic import BaseModel

class MtrCountrySchema(BaseModel):
    is_active:Optional[bool]=None 
    country_id:Optional[int]=None
    country_code:str
    country_name:str
    country_language:str
    country_phone:str
    currency_id:int

    class Config:
        orm_mode = True

class MtrCountryRequest(BaseModel):
    country_code:str
    country_name:str
    country_language:str
    country_phone:str
    currency_id:int

class MtrCountryResponses(BaseModel):
    status_code:int
    msg_status:str
    data:List[MtrCountrySchema]

class MtrCountryResponse(BaseModel):
    status_code:int
    msg_status:str
    data:MtrCountrySchema
