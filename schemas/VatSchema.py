from pydantic import BaseModel
from datetime import datetime

class VatCompanyRequest(BaseModel):
    vat_same_company_id:int
    vat_npwp_no:str
    vat_npwp_date:datetime
    vat_tax_branch_code:str
    vat_name:str
    vat_reserve:str
    vat_pkp_type:str
    vat_pkp_no:str
    vat_pkp_date:datetime
    vat_address_id:int
    vat_tax_out_transaction_id:int
    vat_kpp_id:int

class VatCompanySchema(VatCompanyRequest):
    is_active:bool
    vat_id:int