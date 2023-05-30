from typing import List, Optional
from pydantic import BaseModel

class MtrGeneralLedgerProcessGetSchema(BaseModel):
    general_ledger_process_code:Optional[str] = None
    general_ledger_process_name:Optional[str] = None
    
    class Config:
        orm_mode = True