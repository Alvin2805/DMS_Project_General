from sqlalchemy import Identity, String,Column,Integer, Boolean
from src.configs.database import Base

class MtrSalesGrade(Base):
    __tablename__ = 'mtr_sales_grade'

    sales_grade_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, default=True, nullable=False)
    sales_grade_code = Column(String(10),nullable=False, unique=True)
    sales_grade_name = Column(String(50),nullable=False)