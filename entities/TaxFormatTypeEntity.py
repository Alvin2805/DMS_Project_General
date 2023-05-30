from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrTaxFormatType(Base):
    __tablename__ = 'mtr_tax_format_type'

    is_active = Column(Boolean, default=True, nullable=False)
    tax_format_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    tax_format_type_code = Column(String(20), nullable=False, unique=True)
    tax_format_type_name = Column(String(256), nullable=False,)