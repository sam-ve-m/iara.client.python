from enum import Enum

from iara_client.domain.schemas.base import BaseSchema


class SchemaOptions(Enum):
    CAF_CPF_VALIDATION = BaseSchema
    CAF_SELFIE_VALIDATION = BaseSchema
    CAF_DOCUMENT_VALIDATION = BaseSchema
    SINACOR_REGISTRATION = BaseSchema
    SINACOR_UPDATE = BaseSchema
    SOLUTIONTECH_SYNC_REGISTER = BaseSchema
    DW_REGISTRATION = BaseSchema
    DW_UPDATE = BaseSchema
    DW_ACCOUNT = BaseSchema
    DW_DOCUMENT_VALIDATION = BaseSchema
    OURO_INVESTE_BASIC_REGISTRATION = BaseSchema
    OURO_INVESTE_UPGRADE_REGISTRATION = BaseSchema
    BANKPRO_REGISTRATION = BaseSchema
    EMAIL_VALIDATION = BaseSchema
    SOCIAL_PROSPECT_REGISTRATION = BaseSchema
