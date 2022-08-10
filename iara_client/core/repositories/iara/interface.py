from abc import ABC, abstractmethod

from iara_client.domain.enums.topics import IaraTopics


class IIaraRepository(ABC):
    @classmethod
    @abstractmethod
    async def send_to_iara(cls, topic: IaraTopics, message: dict) -> bool:
        pass
