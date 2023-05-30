from typing import List, Optional
from pydantic import BaseModel

class MtrUnitOfMeasurementItemGetSchema(BaseModel):
    unit_of_measurement_item_code:Optional[str] = None
    unit_of_measurement_item_name:Optional[str] = None
    
    class Config:
        orm_mode = True