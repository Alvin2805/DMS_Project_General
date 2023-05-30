from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBusinessType(Base):
    __tablename__ = 'mtr_business_type'

    is_active = Column(Boolean, default=True, nullable=False)
    business_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    business_type_code = Column(String(20), nullable=False, unique=True)
    business_type_name = Column(String(256), nullable=False)
