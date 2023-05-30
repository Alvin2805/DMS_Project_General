from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSkillLevel(Base):
    __tablename__ = 'mtr_skill_level'

    is_active = Column(Boolean, default=True, nullable=False)
    skill_level_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    skill_level_code = Column(String(1), nullable=False, unique=True)