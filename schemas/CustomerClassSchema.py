from typing import List, Optional
from pydantic import BaseModel

class MtrCustomerClassGetSchema(BaseModel):
    customer_class_code:Optional[str] = None
    customer_class_name:Optional[str] = None
    
    class Config:
        orm_mode = True