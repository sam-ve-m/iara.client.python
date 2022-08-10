from typing import Tuple

from iara_client.domain.enums.status import IaraClientStatus
from iara_client.domain.enums.topics import Topics
from iara_client.domain.exceptions import (
    InvalidMessage,
    InvalidSchemaName,
    SchemaNotFound,
)
from iara_client.services.schema_validator import SchemaValidatorServiceService
from iara_client.repositories.iara import IaraRepository
from iara_client.core.services.iara import IIaraService

from etria_logger import Gladsheim


class IaraService(IIaraService):

    kafka = IaraRepository
    schema_validator = SchemaValidatorServiceService

    @classmethod
    async def send_to_iara(
        cls, topic: Topics, message: dict, schema_name: str
    ) -> Tuple[bool, IaraClientStatus]:
        is_message_sent = False
        try:
            cls.schema_validator.schema_validator(
                message=message, schema_name=schema_name
            )

            is_message_sent = await cls.kafka.send_to_iara(
                topic=topic, message=message
            )

            return is_message_sent, IaraClientStatus.success

        except InvalidMessage as err:
            error_message = f"{cls.__class__}::send_to_persephone::InvalidMessage"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, IaraClientStatus.invalid_message

        except InvalidSchemaName as err:
            error_message = f"{cls.__class__}::send_to_persephone::InvalidSchemaName"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, IaraClientStatus.invalid_schema_name

        except SchemaNotFound as err:
            error_message = f"{cls.__class__}::send_to_persephone::SchemaNotFound"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, IaraClientStatus.schema_not_found

        except Exception as err:
            error_message = f"{cls.__class__}::send_to_persephone::Exception"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, IaraClientStatus.not_mapped_error
