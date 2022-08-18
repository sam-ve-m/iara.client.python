from enum import Enum


class IaraTopics(Enum):
    BANKPRO_REGISTRATION = "jormungandr-iara.onboarding.bankpro-registration"
    CAF_CPF_VALIDATION = "jormungandr-iara.onboarding.caf-cpf-validation"
    CAF_SELFIE_VALIDATION = "jormungandr-iara.onboarding.caf-selfie-validation"
    CAF_DOCUMENT_VALIDATION = "jormungandr-iara.onboarding.caf-document-validation"
    EMAIL_VALIDATION = "jormungandr-iara.onboarding.email-validation"
    DW_DOCUMENT_VALIDATION = "jormungandr-iara.onboarding.dw-document-validation"
    DW_REGISTRATION = "jormungandr-iara.onboarding.dw-registration"
    DW_ACCOUNT = "jormungandr-iara.onboarding.dw-account"
    DW_UPDATE = "jormungandr-iara.onboarding.dw-update"
    OURO_INVESTE_BASIC_REGISTRATION = (
        "jormungandr-iara.onboarding.ouro-investe-basic-registration"
    )
    OURO_INVESTE_UPGRADE_REGISTRATION = (
        "jormungandr-iara.onboarding.ouro-investe-upgrade-registration"
    )
    SINACOR_REGISTRATION = "jormungandr-iara.onboarding.sinacor-registration"
    SINACOR_UPDATE = "jormungandr-iara.onboarding.sinacor-update"
    SOLUTIONTECH_SYNC_REGISTER = (
        "jormungandr-iara.onboarding.solutiontech-sync-register"
    )
