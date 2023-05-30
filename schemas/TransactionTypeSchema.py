from typing import List, Optional
from pydantic import BaseModel

class MtrTransactionTypeGetSchema(BaseModel):
    transaction_type_code:Optional[str] = None
    transaction_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True