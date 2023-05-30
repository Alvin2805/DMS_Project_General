from sqlalchemy import Column,Boolean,String,Integer,CHAR
from sqlalchemy.orm import relationship
from src.configs.database import Base,engine

class MtrTermOfPayment(Base):
    __tablename__ = "mtr_term_of_payment"
    is_active = Column(Boolean,nullable=False,default=True)
    term_of_payment_id = Column(Integer,primary_key=True)
    term_of_payment_code = Column(String(5),nullable=False,unique=True)
    term_of_payment_installment = Column(Integer,nullable=True,default=0)
    term_of_payment_interval = Column(Integer,nullable=True,default=0)
    term_of_payment_name = Column(String(100),nullable=True,default="")
    term_of_payment_policy = Column(CHAR(1),nullable=True,default="")

    company_term_of_payment = relationship("MtrCompany",back_populates="term_of_payment_company",foreign_keys="MtrCompany.term_of_payment_id")
