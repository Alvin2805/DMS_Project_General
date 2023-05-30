from sqlalchemy import Column, Identity,Integer,String, Boolean, DateTime
from src.configs.database import Base

class MtrLogging(Base):
    __tablename__ = 'mtr_logging'
    logging_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(5),nullable=False)
    changed_at = Column(DateTime)
    changed_by = Column(String(5))
    hitted_apis = Column(String(5),nullable=False)
    http_requests = Column(String(10),nullable=False)
    http_respons = Column(String(10),nullable=False)
    data_context = Column(String(20),nullable=False)
    triggered_menu = Column(String(50),nullable=False)
    ip_address = Column(String(50), nullable=False)
