from sqlalchemy import String,Column,Float,Integer, Boolean
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrAddress(Base):
    __tablename__ = "mtr_address"
    is_active = Column(Boolean,nullable=False,default=True)
    address_id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    address_latitude = Column(Float,nullable=True,default=0)
    address_longitude = Column(Float,nullable=True,default=0)
    address_street = Column(String(100),nullable=False)
    address_type = Column(String(5),nullable=True,default="Test")

    company_address = relationship("MtrCompany",back_populates="address_company", foreign_keys="MtrCompany.company_office_address_id")
    vat_address = relationship("MtrVatCompany",back_populates="address_vat",foreign_keys="MtrVatCompany.vat_address_id")
    tax_address = relationship("MtrCompany",back_populates="address_tax",foreign_keys="MtrCompany.tax_address_id")