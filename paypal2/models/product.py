from typing import Optional, Literal

from pydantic import BaseModel, Field


class _ProductMinimalCommon(BaseModel):
    id: Optional[str] = Field(min_length=6, max_length=50)
    name: Optional[str] = Field(min_length=1, max_length=127)
    description: Optional[str] = Field(min_length=1, max_length=256)


class _ProductCommon(_ProductMinimalCommon):
    type: Optional[Literal["DIGITAL", "PHYSICAL", "SERVICE"]] = Field(min_length=1, max_length=24)
    category: Optional[str] = Field(min_length=4, max_length=256, pattern=r"^[A-Z_]+$")
    image_url: Optional[str] = Field(min_length=1, max_length=2000)
    home_url: Optional[str] = Field(min_length=1, max_length=2000)


class ProductDetails(_ProductCommon):
    pass
    # todo links
    # todo create_time
    # todo update_time


class ProductCreate(_ProductCommon):
    name: str = Field(min_length=1, max_length=127)
    type: Literal["DIGITAL", "PHYSICAL", "SERVICE"] = Field(min_length=1, max_length=24)


class ProductListProduct(_ProductMinimalCommon):
    pass
    # todo links
    # todo create_time


class ProductList(BaseModel):
    products: list[ProductListProduct]
    total_items: int
    total_pages: int
    # todo links
