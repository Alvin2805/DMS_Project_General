from typing import List, Optional
from pydantic import BaseModel

class MtrTransactionTypeCashManagementOutGetSchema(BaseModel):
    transaction_type_cash_management_out_code:Optional[str] = None
    transaction_type_cash_management_out_name:Optional[str] = None
    
    class Config:
        orm_mode = True