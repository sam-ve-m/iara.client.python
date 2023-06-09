from typing import Optional

from iara_client.domain.schemas.base import BaseSchema


class ScoreValidationSchema(BaseSchema):
    device_info: Optional[dict]
    device_id: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    precision: Optional[float]
    ip_address: Optional[str]
