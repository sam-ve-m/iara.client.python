from enum import Enum

from iara_client.domain.schemas.base import BaseSchema


class ChooseSchema(Enum):
    caf_cpf_validation = BaseSchema
    caf_selfie_validation = BaseSchema
    caf_document_validation = BaseSchema
    sinacor_registration = BaseSchema
    sinacor_update = BaseSchema
    solutiontech_sync_register = BaseSchema
    dw_registration = BaseSchema
    dw_update = BaseSchema
    dw_document_validation = BaseSchema
    ouro_investe_basic_registration = BaseSchema
    ouro_investe_upgrade_registration = BaseSchema
    bankpro_registration = BaseSchema
    send_confirmation_email = BaseSchema
    social_prospect_registration = BaseSchema
