from iara_client.core.repositories.iara import IIaraRepository
from iara_client.domain.enums.topics import IaraTopics
from iara_client.infraestructure.kafka import KafkaInfrastructure

from etria_logger import Gladsheim
from nidavellir import Sindri


from aiokafka.errors import KafkaTimeoutError, KafkaError
from orjson import dumps


class IaraRepository(IIaraRepository):

    infra = KafkaInfrastructure

    @classmethod
    async def send_to_iara(cls, topic: IaraTopics, message: dict) -> bool:
        is_message_sent = True
        record_metadata = None

        try:
            kafka_producer = await cls.infra.get_or_create_producer()
            message = dumps(message, default=Sindri.dict_to_primitive_types)
            record_metadata = await kafka_producer.send_and_wait(
                topic=topic.value, value=message
            )

        except KafkaTimeoutError as err:
            message = f"{cls.__class__}::send_to_persephone::KafkaTimeoutError::is_message_sent:{is_message_sent}::record metadata:{record_metadata}"
            is_message_sent = False
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        except KafkaError as err:
            message = f"{cls.__class__}::send_to_persephone::KafkaError::is_message_sent:{is_message_sent}::record metadata:{record_metadata}"
            is_message_sent = False
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        except Exception as err:
            message = f"{cls.__class__}::send_to_persephone::Exception::is_message_sent:{is_message_sent}::record metadata:{record_metadata}"
            is_message_sent = False
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        return is_message_sent
