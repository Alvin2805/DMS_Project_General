from typing import List, Optional
from pydantic import BaseModel

class MtrAfterSalesAreaGetSchema(BaseModel):
    after_sales_area_code:Optional[str] = None
    after_sales_area_name:Optional[str] = None
    
    class Config:
        orm_mode = True