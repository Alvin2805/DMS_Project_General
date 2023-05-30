
from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrUnitOfMeasurementItem(Base):
    __tablename__ = 'mtr_unit_of_measurement_item'
    

    is_active = Column(Boolean, default=True, nullable=False)
    unit_of_measurement_item_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    unit_of_measurement_item_code = Column(String(10), nullable=False, unique=True)
    unit_of_measurement_item_name = Column(String(50), nullable=False)