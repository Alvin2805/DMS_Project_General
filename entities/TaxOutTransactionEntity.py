from sqlalchemy import Column,Boolean,String,Integer
from sqlalchemy.orm import relationship
from src.configs.database import Base, engine

class MtrTaxOutTransaction(Base):
    __tablename__ = "mtr_tax_out_transaction"
    is_active = Column(Boolean,nullable=False,default=True)
    tax_out_transaction_id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    tax_out_transaction_code = Column(String(20),nullable=False)
    tax_out_transaction_name = Column(String(256),nullable=True,default="")

    vat_company_taxouttrans = relationship("MtrVatCompany",back_populates="taxouttrans_vat_company",foreign_keys="MtrVatCompany.vat_tax_out_transaction_id")