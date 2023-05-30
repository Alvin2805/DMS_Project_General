from sqlalchemy import Column, Identity,Integer,Boolean,String
from src.configs.database import Base

class MtrAdjustmentReason(Base):
    __tablename__ = 'mtr_adjustment_reason'
    is_active = Column(Boolean, default=True, nullable=False)
    adjustment_reason_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    adjustment_reason_code = Column(String(20),nullable=False, unique=True)
    adjustment_reason_name = Column(String(256), nullable=False)