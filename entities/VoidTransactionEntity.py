from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrVoidTransaction(Base):
    __tablename__ = 'mtr_void_transaction'
    

    is_active = Column(Boolean, default=True, nullable=False)
    void_transaction_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    void_transaction_code = Column(String(20), nullable=False, unique=True)
    void_transaction_name = Column(String(256), nullable=False,)