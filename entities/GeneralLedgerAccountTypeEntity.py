from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrGeneralLedgerAccountType(Base):
    __tablename__ = 'mtr_general_ledger_account_type'

    is_active = Column(Boolean, default=True, nullable=False)
    general_ledger_account_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    general_ledger_account_type_code = Column(String(20), nullable=False, unique=True)
    general_ledger_account_type_name = Column(String(256), nullable=False)
