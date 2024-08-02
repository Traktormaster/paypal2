from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field


class _ProductMinimalCommon(BaseModel):
    id: Optional[str] = Field(min_length=6, max_length=50, default=None)
    name: Optional[str] = Field(min_length=1, max_length=127, default=None)
    description: Optional[str] = Field(min_length=1, max_length=256, default=None)


class _ProductCommon(_ProductMinimalCommon):
    type: Optional[Literal["DIGITAL", "PHYSICAL", "SERVICE"]] = Field(min_length=1, max_length=24, default=None)
    category: Optional[str] = Field(min_length=4, max_length=256, pattern=r"^[A-Z_]+$", default=None)
    image_url: Optional[str] = Field(min_length=1, max_length=2000, default=None)
    home_url: Optional[str] = Field(min_length=1, max_length=2000, default=None)


class ProductDetails(_ProductCommon):
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    # todo links


class ProductCreate(_ProductCommon):
    name: str = Field(min_length=1, max_length=127)
    type: Literal["DIGITAL", "PHYSICAL", "SERVICE"] = Field(min_length=1, max_length=24)


class ProductListProduct(_ProductMinimalCommon):
    create_time: Optional[datetime] = None
    # todo links


class ProductList(BaseModel):
    products: list[ProductListProduct]
    total_items: Optional[int] = None
    total_pages: Optional[int] = None
    # todo links
