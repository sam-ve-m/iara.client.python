from etria_logger import Gladsheim

from iara_client.domain.enums.schema.options import SchemaOptions
from iara_client.domain.enums.schema.types import SchemaTypes
from iara_client.domain.exceptions import SchemaNotFound
from iara_client.core.services.message_validator import IMessageValidatorService
from pydantic import ValidationError


class MessageValidatorService(IMessageValidatorService):
    @staticmethod
    def __apply_schema(schema: SchemaOptions, message: dict) -> bool:
        try:
            schema_to_apply = schema.value
            schema_to_apply(**message)
            return True
        except ValidationError as error:
            Gladsheim.error(error, exc_info=True)
            return False

    @staticmethod
    def __get_schema(schema_to_use: SchemaTypes) -> SchemaOptions:
        try:
            exists_schema = SchemaOptions[schema_to_use.name]
            return exists_schema
        except Exception as e:
            raise SchemaNotFound(msg=f"Schema {schema_to_use} not exists.")

    @staticmethod
    def validate_message(message: dict, schema_type: SchemaTypes) -> bool:
        schema_to_apply: SchemaOptions = MessageValidatorService.__get_schema(
            schema_type
        )
        is_valid_message = MessageValidatorService.__apply_schema(
            schema=schema_to_apply, message=message
        )
        return is_valid_message
