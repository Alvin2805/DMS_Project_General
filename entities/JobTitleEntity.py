from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrJobTitle(Base):
    __tablename__ = 'mtr_job_title'

    is_active = Column(Boolean, default=True, nullable=False)
    job_title_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    job_title_code = Column(String(5), nullable=False, unique=True)
    job_title_name = Column(String(100), nullable=False)
    