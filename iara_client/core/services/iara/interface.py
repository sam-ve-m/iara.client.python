from abc import ABC, abstractmethod
from typing import Tuple

from iara_client.domain.enums.status import IaraClientStatus


class IIaraService(ABC):
    @classmethod
    @abstractmethod
    async def send_to_persephone(
        cls, topic: str, partition: int, message: dict, schema_name: str
    ) -> Tuple[bool, IaraClientStatus]:
        pass
