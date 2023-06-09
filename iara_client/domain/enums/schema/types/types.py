from enum import Enum


class SchemaTypes(Enum):
    CAF_CPF_VALIDATION = "caf_cpf_validation"
    CAF_CPF_VALIDATION_DETAILS = "caf_cpf_validation_details"
    CAF_SCORE_VALIDATION = "caf_score_validation"
    CAF_SCORE_VALIDATION_DETAILS = "caf_score_validation_details"
    CAF_DOCUMENT_VALIDATION = "caf_document_validation"
    SINACOR_REGISTRATION = "sinacor_registration"
    SINACOR_UPDATE = "sinacor_update"
    SOLUTIONTECH_SYNC_REGISTER = "solutiontech_sync_register"
    DW_REGISTRATION = "dw_registration"
    DW_UPDATE = "dw_update"
    DW_ACCOUNT = "dw_account"
    DW_DOCUMENT_VALIDATION = "dw_document_validation"
    OURO_INVESTE_BASIC_REGISTRATION = "ouro_investe_basic_registration"
    OURO_INVESTE_BASIC_REGISTRATION_DETAILS = "ouro_investe_basic_registration_details"
    OURO_INVESTE_UPGRADE_REGISTRATION = "ouro_investe_upgrade_registration"
    BANKPRO_REGISTRATION = "bankpro_registration"
    EMAIL_VALIDATION = "email_validation"
    SOCIAL_PROSPECT_REGISTRATION = "social_prospect_registration"
    SINACOR_UPDATE_LIGA_DASH = "sinacor_update_liga_dash"

    def __str__(self):
        return self.value
