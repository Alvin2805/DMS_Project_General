from typing import List, Optional
from pydantic import BaseModel

class MtrBusinessScopeGetSchema(BaseModel):
    business_scope_code:Optional[str] = None
    business_scope_name:Optional[str] = None
    
    class Config:
        orm_mode = True