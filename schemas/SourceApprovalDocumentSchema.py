from typing import List, Optional
from pydantic import BaseModel

class MtrSourceApprovalDocumentGetSchema(BaseModel):
    source_approval_document_code:Optional[str] = None
    source_approval_document_name:Optional[str] = None
    
    class Config:
        orm_mode = True