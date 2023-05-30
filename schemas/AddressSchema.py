from pydantic import BaseModel

class MtrAddressRequest(BaseModel):
    address_latitude:float
    address_longitude:float
    address_street:str
    address_type:str

    class Config:
        orm_mode = True

