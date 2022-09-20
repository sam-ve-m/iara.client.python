from pydantic import BaseModel


class OuroInvestRequirements(BaseModel):
    cpf: str
