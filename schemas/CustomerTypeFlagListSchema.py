from typing import List, Optional
from pydantic import BaseModel

class MtrCustomerTypeFlagListGetSchema(BaseModel):
    customer_type_flag_list_code:Optional[str] = None
    customer_type_flag_list_name:Optional[str] = None
    
    class Config:
        orm_mode = True