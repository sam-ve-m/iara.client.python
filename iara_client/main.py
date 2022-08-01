from typing import Tuple

from iara_client.domain.enums.status import IaraClientStatus
from iara_client.services.iara import IaraService


class Iara:
    @staticmethod
    async def send_to_persephone(
        topic: str, partition: int, message: dict, schema_name: str
    ) -> Tuple[bool, IaraClientStatus]:
        (
            is_message_sent,
            persephone_client_status,
        ) = await IaraService.send_to_persephone(
            topic=topic, partition=partition, message=message, schema_name=schema_name
        )

        return is_message_sent, persephone_client_status