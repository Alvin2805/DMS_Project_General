from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrIncentiveLevel(Base):
    __tablename__ = 'mtr_incentive_level'

    is_active = Column(Boolean, default=True, nullable=False)
    incentive_level_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    incentive_level_variable = Column(String(50))
    incentive_level_code = Column(String(100), nullable=False, unique=True)
    incentive_level_name = Column(String(50), nullable=False)

    