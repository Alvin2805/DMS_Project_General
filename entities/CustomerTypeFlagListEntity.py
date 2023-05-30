from sqlalchemy import CHAR, Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrCustomerTypeFlagList(Base):
    __tablename__ = 'mtr_customer_type_flag_list'

    is_active = Column(Boolean, default=True, nullable=False)
    customer_type_flag_list_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    customer_type_flag_list_code = Column(String(1), nullable=False, unique=True)
    customer_type_flag_list_name = Column(String(20), nullable=False)