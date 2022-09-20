from pydantic import BaseModel


class CafCpfValidationRequirements(BaseModel):
    unique_id: str
    cpf: str


class CafCpfValidationDetailsRequirements(BaseModel):
    unique_id: str
    transaction_id: str


class CafScoreValidationRequirements(BaseModel):
    unique_id: str
    cpf: str


class CafScoreValidationDetailsRequirements(BaseModel):
    unique_id: str
    transaction_id: str
