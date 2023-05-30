from typing import List, Optional
from pydantic import BaseModel

class MtrBusinessGroupGetSchema(BaseModel):
    business_group_code:Optional[str] = None
    business_group_name:Optional[str] = None
    
    class Config:
        orm_mode = True