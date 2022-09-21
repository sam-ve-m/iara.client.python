from enum import Enum


class IaraTopics(Enum):
    CAF_CPF_VALIDATION = "jormungandr-iara.onboarding.caf-cpf-validation"
    CAF_CPF_VALIDATION_DETAILS = "jormungandr-iara.onboarding.caf-cpf-validation-details"
    CAF_SELFIE_VALIDATION = "jormungandr-iara.onboarding.caf-selfie-validation"
    CAF_SELFIE_VALIDATION_DETAILS = "jormungandr-iara.onboarding.caf-selfie-validation-details"
    CAF_DOCUMENT_VALIDATION = "jormungandr-iara.onboarding.caf-document-validation"
    SINACOR_REGISTRATION = "jormungandr-iara.onboarding.sinacor-registration"
    SINACOR_UPDATE = "jormungandr-iara.onboarding.sinacor-update"
    SOLUTIONTECH_SYNC_REGISTER = (
        "jormungandr-iara.onboarding.solutiontech-sync-register"
    )
    DW_REGISTRATION = "jormungandr-iara.onboarding.dw-registration"
    DW_UPDATE = "jormungandr-iara.onboarding.dw-update"
    DW_ACCOUNT = "jormungandr-iara.onboarding.dw-account"
    DW_DOCUMENT_VALIDATION = "jormungandr-iara.onboarding.dw-document-validation"
    OURO_INVESTE_BASIC_REGISTRATION = (
        "jormungandr-iara.onboarding.ouro-investe-basic-registration"
    )
    OURO_INVESTE_BASIC_REGISTRATION_DETAILS = (
        "jormungandr-iara.onboarding.ouro-investe-basic-registration-details"
    )
    OURO_INVESTE_UPGRADE_REGISTRATION = (
        "jormungandr-iara.onboarding.ouro-investe-upgrade-registration"
    )
    BANKPRO_REGISTRATION = "jormungandr-iara.onboarding.bankpro-registration"
    EMAIL_VALIDATION = "jormungandr-iara.onboarding.email-validation"
    SOCIAL_PROSPECT_REGISTRATION = "sphinx-iara.onboarding.social-prospect-registration"
