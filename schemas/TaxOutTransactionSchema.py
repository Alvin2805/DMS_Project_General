from typing import List, Optional
from pydantic import BaseModel

class MtrTaxOutTransactionGetSchema(BaseModel):
    tax_out_transaction_code:Optional[str] = None
    tax_out_transaction_name:Optional[str] = None
    
    class Config:
        orm_mode = True