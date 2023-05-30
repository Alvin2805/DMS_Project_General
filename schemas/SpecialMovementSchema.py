from typing import List, Optional
from pydantic import BaseModel

class MtrSpecialMovementGetSchema(BaseModel):
    special_movement_code:Optional[str] = None
    special_movement_name:Optional[str] = None
    
    class Config:
        orm_mode = True