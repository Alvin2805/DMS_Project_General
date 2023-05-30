from sqlalchemy import Column,String,Integer,Boolean
from sqlalchemy.orm import relationship
from src.configs.database import Base

class MtrCountry(Base):
    __tablename__ = "mtr_country"
    is_active = Column(Boolean,nullable=False,default=True)
    country_id = Column(Integer,primary_key=True)
    country_code = Column(String(5),nullable=False,unique=True)
    country_name = Column(String(100),nullable=False)
    country_language = Column(String(20),nullable=False,default="")
    country_phone = Column(String(15),nullable=False,default="")
    currency_id = Column(Integer,nullable=False) #relation with mtr_currency in finance module

    province_country = relationship("MtrProvince",back_populates="country_province",foreign_keys="MtrProvince.country_id")