from pydantic import BaseModel

class CpfValidationSchema(BaseModel):
    cpf: str
