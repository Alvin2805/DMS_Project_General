from sqlalchemy import Boolean,String,Column,Integer
from sqlalchemy.orm import relationship
from src.configs.database import Base,engine

class MtrIncentiveGroup(Base):
    __tablename__ = "mtr_incentive_group"
    is_active = Column(Boolean,nullable=False,default=True)
    incentive_group_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    incentive_group_code = Column(String(50),nullable=False,unique=True)
    incentive_group_name = Column(String(100),nullable=False)

    company_incentive_group = relationship("MtrCompany",back_populates="incentive_group_company",foreign_keys="MtrCompany.incentive_group_id")