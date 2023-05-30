from sqlalchemy import Boolean,String,CHAR,Integer,Column
from sqlalchemy.orm import relationship
from src.configs.database import Base,engine

class MtrFinanceArea(Base):
    __tablename__ = "mtr_finance_area"
    is_active = Column(Boolean,nullable=False,default=True)
    finance_area_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    finance_area_code = Column(String(20),nullable=False,unique=True)
    finance_area_name = Column(String(256),nullable=True,default="")

    company_finance_area = relationship("MtrCompany",back_populates="finance_area_company", foreign_keys="MtrCompany.finance_area_id")