from iara_client.core.services.schema_validator import ISchemaValidatorService
from iara_client.domain.enums.schema.types import SchemaTypes
from iara_client.domain.exceptions import InvalidMessage, InvalidSchemaName
from iara_client.services.message_validator import MessageValidatorService
from nidavellir.src.uru import Sindri


class SchemaValidatorServiceService(ISchemaValidatorService):
    @staticmethod
    def __validate_message(message: dict):
        if type(message) != dict:
            raise InvalidMessage(msg="Given message must be dict type")

        if type(message) == dict and len(message) < 1:
            raise InvalidMessage(msg="Given message must not be empty")

    @staticmethod
    def __validate_schema(schema_name: dict):
        if type(schema_name) != str:
            raise InvalidSchemaName("Given schema name must be str type")

        if not schema_name:
            raise InvalidSchemaName("Given schema name must not be empty")

    @staticmethod
    def schema_validator(message: dict, schema_type: SchemaTypes):
        message = Sindri.dict_to_primitive_types(message)
        is_valid_message = MessageValidatorService.validate_message(
            message=message, schema_type=schema_type
        )

        if not is_valid_message:
            raise InvalidMessage(
                msg=f"Given message must be compatible with schema {schema_type}"
            )
