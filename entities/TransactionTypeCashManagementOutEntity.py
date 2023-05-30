from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrTransactionTypeCashManagementOut(Base):
    __tablename__ = 'mtr_transaction_type_cash_management_out'
    

    is_active = Column(Boolean, default=True, nullable=False)
    transaction_type_cash_management_out_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    transaction_type_cash_management_out_code = Column(String(20), nullable=False, unique=True)
    transaction_type_cash_management_out_name = Column(String(256), nullable=False,)
