from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrWorkOrderTransactionType(Base):
    __tablename__ = 'mtr_work_order_transaction_type'
    

    is_active = Column(Boolean, default=True, nullable=False)
    work_order_transaction_type_id = Column(Integer, primary_key=True)
    work_order_transaction_type_code = Column(String(20), nullable=False, unique=True)
    work_order_transaction_type_name = Column(String(256), nullable=False)
