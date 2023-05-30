from typing import List, Optional
from pydantic import BaseModel

class MtrGeneralLedgerDimensionTypeGetSchema(BaseModel):
    general_ledger_dimension_type_code:Optional[str] = None
    general_ledger_dimension_type_name:Optional[str] = None
    
    class Config:
        orm_mode = True