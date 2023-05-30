from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrBrandType(Base):
    __tablename__ = 'mtr_brand_type'

    is_active = Column(Boolean, default=True, nullable=False)
    brand_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    brand_type_code = Column(String(20), nullable=False, unique=True)
    brand_type_name = Column(String(256), nullable=False)