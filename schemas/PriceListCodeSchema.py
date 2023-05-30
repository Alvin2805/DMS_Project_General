from typing import List, Optional
from pydantic import BaseModel

class MtrPriceListCodeGetSchema(BaseModel):
    price_list_code:Optional[str] = None
    price_list_code_name:Optional[str] = None
    
    class Config:
        orm_mode = True