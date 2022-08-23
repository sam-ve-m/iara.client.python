from enum import Enum

from iara_client.domain.schemas.base import BaseSchema


class SchemaOptions(Enum):
    BANKPRO_REGISTRATION = BaseSchema
    CAF_CPF_VALIDATION = BaseSchema
    CAF_SELFIE_VALIDATION = BaseSchema
    CAF_DOCUMENT_VALIDATION = BaseSchema
    EMAIL_VALIDATION = BaseSchema
    DW_DOCUMENT_VALIDATION = BaseSchema
    DW_REGISTRATION = BaseSchema
    DW_ACCOUNT = BaseSchema
    DW_UPDATE = BaseSchema
    OURO_INVESTE_BASIC_REGISTRATION = BaseSchema
    OURO_INVESTE_UPGRADE_REGISTRATION = BaseSchema
    SINACOR_REGISTRATION = BaseSchema
    SINACOR_UPDATE = BaseSchema
    SOLUTIONTECH_SYNC_REGISTER = BaseSchema
    SOCIAL_PROSPECT_REGISTRATION = BaseSchema

