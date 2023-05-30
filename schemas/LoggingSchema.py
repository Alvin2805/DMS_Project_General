from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class MtrLoggingPostSchema(BaseModel):
    created_at:Optional[str] = None
    created_by:Optional[datetime] = None
    hitted_apis:Optional[str] = None
    http_requests:Optional[str] = None
    http_respons:Optional[str] = None
    data_context:Optional[str] = None
    triggered_menu:Optional[str] = None
    ip_address:Optional[str] = None
    class Config:
        orm_mode = True

class MtrLoggingPutSchema(BaseModel):
    changed_at:Optional[str] = None
    changed_by:Optional[datetime] = None
    hitted_apis:Optional[str] = None
    http_requests:Optional[str] = None
    http_respons:Optional[str] = None
    data_context:Optional[str] = None
    triggered_menu:Optional[str] = None
    ip_address:Optional[str] = None
    class Config:
        orm_mode = True