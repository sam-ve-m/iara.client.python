from pydantic import BaseModel
from iara_client.domain.schemas.base import BaseSchema


class DeviceInformation(BaseModel):
    dt: int
    cm_fl: bool
    mp: int
    cm_num: int
    p_count: int
    acc_n: str
    acc_v: str
    bd: str
    hw: str
    md: str
    boa: str
    cpu: str
    md_name: str
    p_mem: int
    nfc: bool
    bio: bool
    iim: str


class SelfieValidationSchema(BaseSchema):
    device_info: DeviceInformation
    device_id: str
    latitude: int
    longitude: int
    precision: int
    ip_address: str
