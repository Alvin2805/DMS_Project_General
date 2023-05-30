from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBusinessGroup(Base):
    __tablename__ = 'mtr_business_group'

    is_active = Column(Boolean, default=True, nullable=False)
    business_group_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_group_code = Column(String(10), nullable=False, unique=True)
    business_group_name = Column(String(50), nullable=False)