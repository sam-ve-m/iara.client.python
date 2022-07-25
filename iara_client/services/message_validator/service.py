from etria_logger import Gladsheim

from iara_client.domain.exceptions import SchemaNotFound
from iara_client.domain.enums.schema import ChooseSchema
from iara_client.core.services.message_validator import IMessageValidatorService
from pydantic import ValidationError


class MessageValidatorService(IMessageValidatorService):
    @staticmethod
    def __apply_schema(schema_to_apply: any, message: dict) -> bool:
        try:
            schema_to_apply(**message)
            return True
        except ValidationError as error:
            Gladsheim.error(error, exc_info=True)
            return False

    @staticmethod
    def __get_schema(schema_to_use: str):
        try:
            exists_schema = ChooseSchema[schema_to_use]
            return exists_schema
        except Exception as e:
            raise SchemaNotFound(msg=f"Schema {schema_to_use} not exists.")

    @staticmethod
    def validate_message(message: dict, schema_name: str) -> bool:
        schema_to_apply = MessageValidatorService.__get_schema(schema_name)
        is_valid_message = MessageValidatorService.__apply_schema(
            schema_to_apply=schema_to_apply.value, message=message
        )
        return is_valid_message
