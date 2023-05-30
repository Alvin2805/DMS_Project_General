from typing import List
from pydantic import BaseModel

class MtrAdjustmentReasonSchema(BaseModel):
    is_active:bool
    adjustment_reason_id:int
    adjustment_reason_code:str
    adjustment_reason_name:str

    class Config:
        orm_mode = True

class MtrAdjustmentReasonResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrAdjustmentReasonSchema]

class MtrAftersalesAreaSchema(BaseModel):
    is_active:bool
    aftersales_area_id:int
    aftersales_area_code:str
    aftersales_area_name:str

    class Config:
        orm_mode = True

class MtrAftersalesAreaResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrAftersalesAreaSchema]

class MtrApprovalCodeSchema(BaseModel):
    is_active:bool
    approval_code_id:int
    approval_code:str
    approval_code_name:str

    class Config:
        orm_mode = True

class MtrApprovalCodeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrApprovalCodeSchema]

class MtrApprovalSpmSchema(BaseModel):
    is_active: bool
    approval_spm_id: int
    approval_spm_code: str
    approval_spm_name: str

    class Config:
        orm_mode = True

class MtrApprovalSpmResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrApprovalSpmSchema]

class MtrBankAccountTypeSchema(BaseModel):
    is_active: bool
    bank_account_type_id: int
    bank_account_type_code: str
    bank_account_type_name: str

    class Config:
        orm_mode = True

class MtrBankAccountTypeResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrBankAccountTypeSchema]

class MtrBillAbleToSchema(BaseModel):
    is_active: bool
    billable_to_id: int
    billable_to_code: str
    billable_to_name: str

    class Config:
        orm_mode = True

class MtrBillAbleToResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrBillAbleToSchema]

class MtrBrandTypeSchema(BaseModel):
    is_active: bool
    brand_type_id: int
    brand_type_code: str
    brand_type_name: str

    class Config:
        orm_mode = True

class MtrBrandTypeResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrBrandTypeSchema]

class MtrBusinessCategorySchema(BaseModel):
    is_active: bool
    business_category_id: int
    business_category_code: str
    business_category_name: str

    class Config:
        orm_mode = True

class MtrBusinessCategoryResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrBusinessCategorySchema]

class MtrBusinessGroupSchema(BaseModel):
    is_active: bool
    business_group_id: int
    group_code: str
    group_name: str

    class Config:
        orm_mode = True

class MtrBusinessGroupResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrBusinessGroupSchema]

class MtrBusinessScopeSchema(BaseModel):
    is_active:bool
    business_scope_id:int
    business_scope_code:str
    business_scope_name:str

    class Config:
        orm_mode = True

class MtrBusinessScopeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrBusinessScopeSchema]


class MtrBusinessTypeSchema(BaseModel):
    is_active:bool
    business_type_id:int
    business_type_code:str
    business_type_name:str

    class Config:
        orm_mode = True

class MtrBusinessTypeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrBusinessTypeSchema]

class MtrCustomerTypeFlagListSchema(BaseModel):
    is_active:bool
    customer_type_flag_list_id:int
    customer_type_flag_list_code:str
    customer_type_flag_list_name:str

    class Config:
        orm_mode = True

class MtrCustomerTypeFlagListResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrCustomerTypeFlagListSchema]

class MtrFinanceAreaSchema(BaseModel):
    is_active:bool
    finance_area_id:int
    finance_area_code:str
    finance_area_name:str

    class Config:
        orm_mode = True

class MtrFinanceAreaResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrFinanceAreaSchema]

class MtrGeneralLedgerAccTypeSchema(BaseModel):
    is_active:bool
    general_ledger_acc_type_id:int
    general_ledger_acc_type_code:str
    general_ledger_acc_type_name:str

    class Config:
        orm_mode = True

class MtrGeneralLedgerAccTypeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrGeneralLedgerAccTypeSchema]

class MtrGeneralLedgerDimTypeSchema(BaseModel):
    is_active:bool
    general_ledger_dim_type_id:int
    general_ledger_dim_type_code:str
    general_ledger_dim_type_name:str

    class Config:
        orm_mode = True

class MtrGeneralLedgerDimTypeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrGeneralLedgerDimTypeSchema]

class MtrIncentiveLevelSchema(BaseModel):
    incentive_level_id:int
    is_active:bool
    incentive_level_variable:str
    incentive_level_code:str
    incentive_level_name:str

    class Config:
        orm_mode = True

class MtrIncentiveLevelResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrIncentiveLevelSchema]


class MtrItemGroupSchema(BaseModel):
    is_active:bool
    item_group_id:int
    item_group_code:str
    item_group_name:str

    class Config:
        orm_mode = True

class MtrItemGroupResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrItemGroupSchema]


class MtrJobPositionSchema(BaseModel):
    is_active: bool
    job_position_id:int
    job_position_code:str
    job_position_name:str

    class Config:
        orm_mode = True

class MtrJobPositionResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrJobPositionSchema]


class MtrJobTitleSchema(BaseModel):
    is_active:bool
    job_title_id:int
    job_title_code:str
    job_title_name:str

    class Config:
        orm_mode = True

class MtrJobTitleResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrJobTitleSchema]


class MtrLineTypeSchema(BaseModel):
    is_active:bool
    line_type_id:int
    line_type_code:str
    line_type_name:str

    class Config:
        orm_mode = True

class MtrLineTypeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrLineTypeSchema]

class MtrPriceListCodeSchema(BaseModel):
    is_active: bool
    price_list_id:int
    price_list_code:str
    price_list_code_name:str

    class Config:
        orm_mode = True

class MtrPriceListCodeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrPriceListCodeSchema]

class MtrReferenceTypePrSchema(BaseModel):
    is_active: bool
    reference_type_id:int
    reference_type_code:str
    reference_type_name:str

    class Config:
        orm_mode = True

class MtrReferenceTypePrResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrReferenceTypePrSchema]

class MtrSalesGradeSchema(BaseModel):
    sales_grade_id:int
    is_active:bool
    sales_grade_code:str
    sales_grade_name:str

    class Config:
        orm_mode = True

class MtrSalesGradeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrSalesGradeSchema]

class MtrSkillLevelSchema(BaseModel):
    is_active: bool
    skill_level_id:int
    skill_level_code:str

    class Config:
        orm_mode = True

class MtrSkillLevelResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrSkillLevelSchema]

class MtrSkillLevelCodeSchema(BaseModel):
    is_active: bool
    skill_level_code_id:int
    skill_level_code:str

    class Config:
        orm_mode = True

class MtrSkillLevelCodeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrSkillLevelCodeSchema]

class MtrSourceApprovalDocumentSchema(BaseModel):
    source_approval_document_id:int
    source_approval_document_code:str
    is_active:bool
    source_approval_document_name:str

    class Config:
        orm_mode = True

class MtrSourceApprovalDocumentResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrSourceApprovalDocumentSchema]

class MtrSpecialMovementSchema(BaseModel):
    is_active: bool
    special_movement_id:int
    special_movement_code:str
    special_movement_name:str

    class Config:
        orm_mode = True

class MtrSpecialMovementResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrSpecialMovementSchema]

class MtrSubstituteTypeSchema(BaseModel):
    is_active:bool
    substitute_type_code:str
    substitute_type_name:str

    class Config:
        orm_mode = True

class MtrSubstituteTypeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrSubstituteTypeSchema]

class MtrTaxFormatTypeSchema(BaseModel):
    is_active: bool
    tax_format_type_id:int
    tax_format_type_code:str
    tax_format_type_name:str

    class Config:
        orm_mode = True

class MtrTaxFormatTypeResponse(BaseModel):
    status:str
    results:int
    payloads:List[MtrTaxFormatTypeSchema]

class MtrTaxOutTransactionSchema(BaseModel):
    is_active: bool
    tax_out_transaction_id: int
    tax_out_transaction_code: str
    tax_out_transaction_name: str

    class Config:
        orm_mode = True

class MtrTaxOutTransactionResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrTaxOutTransactionSchema]

class MtrTransactionTypeSchema(BaseModel):
    transaction_type_id: int
    transaction_type_code: str
    is_active: bool
    transaction_type_name: str

    class Config:
        orm_mode = True

class MtrTransactionTypeResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrTransactionTypeSchema]

class MtrTransactionTypeCashManagementOutSchema(BaseModel):
    is_active: bool
    transaction_type_cash_management_out_id: int
    transaction_type_cash_management_out_code: str
    transaction_type_cash_management_out_name: str

    class Config:
        orm_mode = True

class MtrTransactionTypeCashManagementOutResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrTransactionTypeCashManagementOutSchema]

class MtrUomItemSchema(BaseModel):
    is_active: bool
    uom_item_id: int
    uom_item_code: str
    uom_item_name: str

    class Config:
        orm_mode = True

class MtrUomItemResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrUomItemSchema]

class MtrVoidTransactionSchema(BaseModel):
    is_active: bool
    void_transaction_id: int
    void_transaction_code: str
    void_transaction_name: str

    class Config:
        orm_mode = True

class MtrVoidTransactionResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrVoidTransactionSchema]

class MtrWorkorderTransactionTypeSchema(BaseModel):
    is_active: bool
    workorder_transaction_type_id: int
    workorder_transaction_type_code: str
    workorder_transaction_type_name: str

    class Config:
        orm_mode = True

class MtrWorkorderTransactionTypeResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrWorkorderTransactionTypeSchema]

class MtrWorkorderTypeSchema(BaseModel):
    is_active: bool
    workorder_type_id: int
    workorder_type_code: str
    workorder_type_name: str

    class Config:
        orm_mode = True

class MtrWorkorderTypeResponse(BaseModel):
    status: str
    results: int
    payloads: List[MtrWorkorderTypeSchema]