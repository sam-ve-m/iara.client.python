from abc import ABC, abstractmethod
from typing import Tuple

from iara_client.domain.enums.status import IaraClientStatus
from iara_client.domain.enums.topics import Topics


class IIaraService(ABC):
    @classmethod
    @abstractmethod
    async def send_to_iara(
        cls, topic: Topics, message: dict, schema_name: str
    ) -> Tuple[bool, IaraClientStatus]:
        pass
