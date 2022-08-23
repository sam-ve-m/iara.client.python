from abc import ABC, abstractmethod
from typing import Tuple

from iara_client.domain.enums.status import IaraClientStatus
from iara_client.domain.enums.topics import IaraTopics


class IIaraService(ABC):
    @classmethod
    @abstractmethod
    async def send_to_iara(
        cls, topic: IaraTopics, message: dict
    ) -> Tuple[bool, IaraClientStatus]:
        pass
