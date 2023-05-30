from typing import List, Optional
from pydantic import BaseModel

class MtrLineTypeGetSchema(BaseModel):
    line_type_code:Optional[str] = None
    line_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True