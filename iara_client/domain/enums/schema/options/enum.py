from enum import Enum

from iara_client.domain.schemas.base import BaseSchema
from iara_client.domain.schemas.caf.schema import CafCpfValidationDetailsRequirements, CafCpfValidationRequirements, \
    CafScoreValidationDetailsRequirements, CafScoreValidationRequirements
from iara_client.domain.schemas.ouroinvest.schema import OuroInvestRequirements


class SchemaOptions(Enum):
    CAF_CPF_VALIDATION = CafCpfValidationRequirements
    CAF_CPF_VALIDATION_DETAILS = CafCpfValidationDetailsRequirements
    CAF_SELFIE_VALIDATION = CafScoreValidationRequirements
    CAF_SELFIE_VALIDATION_DETAILS = CafScoreValidationDetailsRequirements
    CAF_DOCUMENT_VALIDATION = BaseSchema
    SINACOR_REGISTRATION = BaseSchema
    SINACOR_UPDATE = BaseSchema
    SOLUTIONTECH_SYNC_REGISTER = BaseSchema
    DW_REGISTRATION = BaseSchema
    DW_UPDATE = BaseSchema
    DW_ACCOUNT = BaseSchema
    DW_DOCUMENT_VALIDATION = BaseSchema
    OURO_INVESTE_BASIC_REGISTRATION = BaseSchema
    OURO_INVESTE_BASIC_REGISTRATION_DETAILS = OuroInvestRequirements
    OURO_INVESTE_UPGRADE_REGISTRATION = BaseSchema
    BANKPRO_REGISTRATION = BaseSchema
    EMAIL_VALIDATION = BaseSchema
    SOCIAL_PROSPECT_REGISTRATION = BaseSchema
