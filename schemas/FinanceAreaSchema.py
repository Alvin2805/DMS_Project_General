from typing import List, Optional
from pydantic import BaseModel

class MtrFinanceAreaGetSchema(BaseModel):
    finance_area_code:Optional[str] = None
    finance_area_name:Optional[str] = None
    
    class Config:
        orm_mode = True