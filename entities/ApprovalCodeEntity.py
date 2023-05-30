from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrApprovalCode(Base):
    __tablename__ = 'mtr_approval_code'

    is_active = Column(Boolean, default=True, nullable=False)
    approval_code_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    approval_code = Column(String(20), nullable=False, unique=True)
    approval_code_name = Column(String(256), nullable=False)