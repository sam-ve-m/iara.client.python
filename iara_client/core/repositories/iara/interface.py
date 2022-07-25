from abc import ABC, abstractmethod


class IIaraRepository(ABC):
    @classmethod
    @abstractmethod
    async def send_to_iara(cls, topic: str, partition: int, message: dict) -> bool:
        pass
