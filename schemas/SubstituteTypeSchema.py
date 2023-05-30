from typing import List, Optional
from pydantic import BaseModel

class MtrSubstituteTypeGetSchema(BaseModel):
    substitute_type_code:Optional[str] = None
    substitute_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True