from typing import List, Optional
from pydantic import BaseModel

class MtrIncentiveLevelGetSchema(BaseModel):
    incentive_level_code:Optional[str] = None
    incentive_level_name:Optional[str] = None
    incentive_level_variable:Optional[str] = None
    
    class Config:
        orm_mode = True