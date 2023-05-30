from typing import List, Optional
from pydantic import BaseModel

class MtrWorkOrderTransactionTypeGetSchema(BaseModel):
    work_order_transaction_type_code:Optional[str] = None
    work_order_transaction_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True