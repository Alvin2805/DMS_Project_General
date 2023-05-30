from typing import List, Optional
from pydantic import BaseModel

class MtrReferenceTypePurchaseRequestGetSchema(BaseModel):
    reference_type_purchase_request_code:Optional[str] = None
    reference_type_purchase_request_name:Optional[str] = None
    
    class Config:
        orm_mode = True