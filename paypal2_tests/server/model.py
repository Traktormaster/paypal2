from pydantic import BaseModel


class OrderCreateApiRequest(BaseModel):
    id: str
