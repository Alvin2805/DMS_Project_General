from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSpecialMovement(Base):
    __tablename__ = 'mtr_special_movement'

    is_active = Column(Boolean, default=True, nullable=False)
    special_movement_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    special_movement_code = Column(String(1), nullable=False, unique=True)
    special_movement_name = Column(String(100), nullable=False)