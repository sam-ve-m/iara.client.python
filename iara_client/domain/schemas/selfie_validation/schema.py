from iara_client.domain.schemas.base import BaseSchema


class SelfieValidationSchema(BaseSchema):
    device_info: dict
    device_id: str
    latitude: float
    longitude: float
    precision: float
    ip_address: str
