from sqlalchemy import CHAR, Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCustomerClass(Base):
    __tablename__ = 'mtr_customer_class'

    customer_class_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, default=True, nullable=False)
    customer_class_code = Column(CHAR(3), nullable=False, unique=True)
    customer_class_name = Column(String(20))