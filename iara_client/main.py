from typing import Tuple

from iara_client.domain.enums.status import IaraClientStatus
from iara_client.domain.enums.topics import IaraTopics
from iara_client.services.iara import IaraService


class Iara:
    @staticmethod
    async def send_to_iara(
        topic: IaraTopics, message: dict
    ) -> Tuple[bool, IaraClientStatus]:
        """
        Send to kafka topic a valid message using schema_type to validate it.

        :param topic: Enum instence of IaraTopics
        :param message: dict
        :return: Returns [process_status: bool, iara_status: IaraClientStatus]
        """
        (
            is_message_sent,
            iara_client_status,
        ) = await IaraService.send_to_iara(topic=topic, message=message)

        return is_message_sent, iara_client_status
