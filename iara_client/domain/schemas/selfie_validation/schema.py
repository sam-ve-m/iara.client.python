from iara_client.domain.schemas.base import BaseSchema


class SelfieValidationSchema(BaseSchema):
    device_info: dict
    device_id: str
