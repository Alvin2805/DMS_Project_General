from typing import List, Optional
from pydantic import BaseModel

class MtrItemGroupGetSchema(BaseModel):
    item_group_code:Optional[str] = None
    item_group_name:Optional[str] = None
    
    class Config:
        orm_mode = True