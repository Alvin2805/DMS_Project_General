from pydantic import BaseModel
from datetime import datetime

class MtrCompanyRequest(BaseModel):
    company_code:str
    company_type:str
    company_name:str
    company_abbreviation:str
    company_office_address_id:int
    company_phone_number:str
    company_fax_number:str
    company_email:str
    vat_same_company_id:int
    vat_npwp_no:str
    vat_npwp_date:datetime
    vat_tax_out_transaction_id:int
    vat_tax_branch_code:str
    vat_name:str
    vat_address_id:int
    vat_reserve:str
    vat_pkp_type:str
    vat_pkp_no:str
    vat_pkp_date:datetime
    vat_kpp_id:int
    tax_npwp_no:str
    tax_npwp_data:datetime
    tax_address_id:int
    tax_pkp_type:str
    tax_pkp_no:str
    tax_pkp_date:datetime
    tax_kpp_id:int
    region_id:int
    finance_area_id:int
    area_id:int
    incentive_group_id:int
    aftersales_area_id:int
    company_ownership_id:int
    business_category_id:int
    term_of_payment_id:int
    company_dealer_kia_code:str
    company_no_of_stall:float
    is_distributor:bool