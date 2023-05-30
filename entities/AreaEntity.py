from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from src.configs.database import Base,engine

class MtrArea(Base):
    __tablename__ = "mtr_area"
    is_active = Column(Boolean,nullable=False,default=True)
    area_id = Column(Integer,primary_key=True)
    area_code = Column(String(10),unique=True,nullable=False)
    description = Column(String,nullable=True,default="")
    region_id = Column(Integer,ForeignKey("mtr_region.region_id"))

    region_area = relationship("MtrRegion",back_populates="area_region",foreign_keys=[region_id])
    company_area = relationship("MtrCompany", back_populates="area_company",foreign_keys="MtrCompany.area_id")
