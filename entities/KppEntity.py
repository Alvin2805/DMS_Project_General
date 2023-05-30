from sqlalchemy import Boolean, String, Integer, Column
from sqlalchemy.orm import relationship
from src.configs.database import Base,engine

class MtrKpp(Base):
    __tablename__ = "mtr_kpp"
    is_active = Column(Boolean,nullable=False,default=True)
    kpp_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    kpp_code = Column(String(5),nullable=False,unique=True)
    kpp_name = Column(String(100),nullable=True,default="")
    kpp_phone_no = Column(String(14),nullable=True,default="")

    company_kpp = relationship("MtrCompany",back_populates="kpp_company",foreign_keys="MtrCompany.tax_kpp_id")
    vat_company_kpp = relationship("MtrVatCompany",back_populates="kpp_vat_company",foreign_keys="MtrVatCompany.vat_kpp_id")