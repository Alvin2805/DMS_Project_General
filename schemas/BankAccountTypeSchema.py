from typing import List, Optional
from pydantic import BaseModel

class MtrBankAccountTypeGetSchema(BaseModel):
    bank_account_type_code:Optional[str] = None
    bank_account_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True