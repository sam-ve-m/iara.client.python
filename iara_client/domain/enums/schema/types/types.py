from enum import Enum


class SchemaTypes(Enum):
    CAF_CPF_VALIDATION = "caf_cpf_validation"
    CAF_SELFIE_VALIDATION = "caf_selfie_validation"
    CAF_DOCUMENT_VALIDATION = "caf_document_validation"
    SINACOR_REGISTRATION = "sinacor_registration"
    SINACOR_UPDATE = "sinacor_update"
    SOLUTIONTECH_SYNC_REGISTER = "solutiontech_sync_register"
    DW_REGISTRATION = "dw_registration"
    DW_UPDATE = "dw_update"
    DW_ACCOUNT = "dw_account"
    DW_DOCUMENT_VALIDATION = "dw_document_validation"
    OURO_INVESTE_BASIC_REGISTRATION = "ouro_investe_basic_registration"
    OURO_INVESTE_UPGRADE_REGISTRATION = "ouro_investe_upgrade_registration"
    BANKPRO_REGISTRATION = "bankpro_registration"
    EMAIL_VALIDATION = "email_validation"
    SOCIAL_PROSPECT_REGISTRATION = "social_prospect_registration"

    def __str__(self):
        return self.value
