from abc import ABC, abstractmethod

from iara_client.domain.enums.topics import Topics


class IIaraRepository(ABC):
    @classmethod
    @abstractmethod
    async def send_to_iara(cls, topic: Topics, message: dict) -> bool:
        pass
