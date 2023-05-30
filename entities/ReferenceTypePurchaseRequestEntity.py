from sqlalchemy import String,Column,Integer, Boolean
from src.configs.database import Base

class MtrReferenceTypePurchaseRequest(Base):
    __tablename__ = 'mtr_reference_type_purchase_request'

    is_active = Column(Boolean, default=True, nullable=False)
    reference_type_purchase_request_id = Column(Integer, primary_key=True)
    reference_type_purchase_request_code = Column(String(5), nullable=False, unique=True)
    reference_type_purchase_request_name = Column(String(100), nullable=False,)