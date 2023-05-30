from typing import List, Optional
from pydantic import BaseModel

class MtrJobTitleGetSchema(BaseModel):
    job_title_code:Optional[str] = None
    job_title_name:Optional[str] = None
    
    class Config:
        orm_mode = True