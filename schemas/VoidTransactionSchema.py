from typing import List, Optional
from pydantic import BaseModel

class MtrVoidTransactionGetSchema(BaseModel):
    void_transaction_code:Optional[str] = None
    void_transaction_name:Optional[str] = None
    
    class Config:
        orm_mode = True