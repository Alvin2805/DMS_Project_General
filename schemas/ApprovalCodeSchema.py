from typing import List, Optional
from pydantic import BaseModel

class MtrApprovalCodeGetSchema(BaseModel):
    approval_code:Optional[str] = None
    approval_code_name:Optional[str] = None
    
    class Config:
        orm_mode = True
