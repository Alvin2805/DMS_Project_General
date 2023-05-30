from typing import List, Optional
from pydantic import BaseModel

class MtrBusinessCategoryGetSchema(BaseModel):
    business_category_code:Optional[str] = None
    business_category_name:Optional[str] = None
    
    class Config:
        orm_mode = True