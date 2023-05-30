from typing import List, Optional
from pydantic import BaseModel

class MtrBusinessTypeGetSchema(BaseModel):
    business_type_code:Optional[str] = None
    business_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True