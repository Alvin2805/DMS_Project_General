from typing import List, Optional
from pydantic import BaseModel

class MtrTaxFormatTypeGetSchema(BaseModel):
    tax_format_type_code:Optional[str] = None
    tax_format_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True