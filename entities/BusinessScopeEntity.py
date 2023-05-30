from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base
from sqlalchemy.orm import relationship

class MtrBusinessScope(Base):
    __tablename__ = 'mtr_business_scope'

    is_active = Column(Boolean, default=True, nullable=False)
    business_scope_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_scope_code = Column(String(20), nullable=False, unique=True)
    business_scope_name = Column(String(256), nullable=False)

    company_business_scope = relationship("MtrCompany",back_populates="business_scope_company",foreign_keys="MtrCompany.business_scope_id")
