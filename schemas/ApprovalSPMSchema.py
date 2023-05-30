from typing import List, Optional
from pydantic import BaseModel

class MtrApprovalSPMGetSchema(BaseModel):
    approval_spm_code:Optional[str] = None
    approval_spm_name:Optional[str] = None
    
    class Config:
        orm_mode = True