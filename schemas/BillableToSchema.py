from typing import List, Optional
from pydantic import BaseModel

class MtrBillableToGetSchema(BaseModel):
    billable_to_code:Optional[str] = None
    billable_to_name:Optional[str] = None
    
    class Config:
        orm_mode = True