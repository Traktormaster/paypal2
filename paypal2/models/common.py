from typing import Optional

from pydantic import BaseModel, Field


class MonetaryValue(BaseModel):
    currency_code: str = Field(min_length=3, max_length=3)
    value: str = Field(max_length=32)


class HATEOASLink(BaseModel):
    href: str
    rel: str
    method: Optional[str] = None
