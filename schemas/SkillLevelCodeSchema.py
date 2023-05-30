from typing import List, Optional
from pydantic import BaseModel

class MtrSkillLevelCodeGetSchema(BaseModel):
    skill_level_code:Optional[str] = None
    
    class Config:
        orm_mode = True