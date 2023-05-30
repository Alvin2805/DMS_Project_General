from typing import List, Optional
from pydantic import BaseModel

class MtrBrandTypeGetSchema(BaseModel):
    brand_type_code:Optional[str] = None
    brand_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True