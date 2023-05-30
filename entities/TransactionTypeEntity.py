from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrTransactionType(Base):
    __tablename__ = 'mtr_transaction_type'
    

    transaction_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    transaction_type_code = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    transaction_type_name = Column(String(256), nullable=False,)