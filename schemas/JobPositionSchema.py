from typing import List, Optional
from pydantic import BaseModel

class MtrJobPositionGetSchema(BaseModel):
    job_position_code:Optional[str] = None
    job_position_name:Optional[str] = None
    
    class Config:
        orm_mode = True