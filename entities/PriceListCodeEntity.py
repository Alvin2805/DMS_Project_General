from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrPriceListCode(Base):
    __tablename__ = 'mtr_price_list_code'

    is_active = Column(Boolean, default=True, nullable=False)
    price_list_code_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    price_list_code = Column(String(20), nullable=False, unique=True)
    price_list_code_name = Column(String(256), nullable=False)