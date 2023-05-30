from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSourceApprovalDocument(Base):
    __tablename__ = 'mtr_source_approval_document'

    source_approval_document_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    source_approval_document_code = Column(String(20), nullable=False, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    source_approval_document_name = Column(String(256), nullable=False,)