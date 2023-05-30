from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrJobPosition(Base):
    __tablename__ = 'mtr_job_position'

    is_active = Column(Boolean, default=True, nullable=False)
    job_position_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    job_position_code = Column(String(10), nullable=False, unique=True)
    job_position_name = Column(String(256), nullable=False)