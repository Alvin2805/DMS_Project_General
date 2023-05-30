from sqlalchemy.orm import relationship
from src.configs.database import Base
from sqlalchemy import Column,Integer,String, CHAR, DateTime, Boolean, ForeignKey

class MtrVatCompany(Base):
    __tablename__ = "mtr_vat_company"
    is_active = Column(Boolean, nullable=False, default=True)
    vat_id = Column(Integer, nullable=False, primary_key=True)
    vat_same_company_id = Column(Integer,nullable=True)
    vat_npwp_no = Column(String(35),nullable=False)
    vat_npwp_date = Column(DateTime,nullable=False)
    vat_tax_branch_code = Column(String(10),nullable=True,default="")
    vat_name = Column(String(100),nullable=True,default="")
    vat_reserve = Column(CHAR(1), nullable=True,default="")
    vat_pkp_type = Column(CHAR(1),nullable=True,default="")
    vat_pkp_no = Column(String(30),nullable=True,default="")
    vat_pkp_date = Column(DateTime,nullable=True,default="")
    vat_address_id = Column(Integer,ForeignKey("mtr_address.address_id"))
    vat_tax_out_transaction_id = Column(Integer,ForeignKey("mtr_tax_out_transaction.tax_out_transaction_id"))
    vat_kpp_id = Column(Integer,ForeignKey("mtr_kpp.kpp_id"))

    company_vat = relationship("MtrCompany",back_populates="vat_company",foreign_keys="MtrCompany.vat_company_id")
    address_vat = relationship("MtrAddress",back_populates="vat_address",foreign_keys=[vat_address_id])
    taxouttrans_vat_company = relationship("MtrTaxOutTransaction",back_populates="vat_company_taxouttrans",foreign_keys=[vat_tax_out_transaction_id])
    kpp_vat_company = relationship("MtrKpp",back_populates="vat_company_kpp",foreign_keys=[vat_kpp_id])