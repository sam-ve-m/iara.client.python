from pydantic import BaseModel

from iara_client.domain.schemas.base import BaseSchema


class DeviceInformation(BaseModel):
    device_id: str
    device_name: str
    device_model: str
    is_emulator: bool
    device_operating_system_name: str
    os_sdk_version: str
    device_is_in_root_mode: bool
    device_network_interfaces: str
    public_ip: str
    access_ip: str
    latitude: float
    longitude: float
    precision: float


class SelfieValidationSchema(BaseSchema):
    device_info: DeviceInformation
