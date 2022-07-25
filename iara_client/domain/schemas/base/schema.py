from pydantic import BaseModel, UUID4


class BaseSchema(BaseModel):
    unique_id: UUID4
