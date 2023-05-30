from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base


class MtrBankAccountType(Base):
    __tablename__ = 'mtr_bank_account_type'

    is_active = Column(Boolean, default=True, nullable=False)
    bank_account_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    bank_account_type_code = Column(String(20), nullable=False, unique=True)
    bank_account_type_name = Column(String(256), nullable=False)