from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrLineType(Base):
    __tablename__ = 'mtr_line_type'

    is_active = Column(Boolean, default=True, nullable=False)
    line_type_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    line_type_code = Column(String(5), nullable=False, unique=True)
    line_type_name = Column(String(100), nullable=False)