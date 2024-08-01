from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field

from paypal2.models.common import HATEOASLink, MonetaryValue


class CapturedPayment(BaseModel):
    id: str
    status: Literal["COMPLETED", "DECLINED", "PARTIALLY_REFUNDED", "PENDING", "REFUNDED", "FAILED"]
    # todo status_details
    invoice_id: Optional[str] = None
    custom_id: Optional[str] = Field(max_length=127, default=None)
    final_capture: Optional[bool] = None
    disbursement_mode: Optional[Literal["INSTANT", "DELAYED"]] = Field(
        min_length=1, max_length=16, pattern=r"^[A-Z_]+$", default="INSTANT"
    )
    links: list[HATEOASLink]
    amount: Optional[MonetaryValue] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    # todo network_transaction_reference
    # todo seller_protection
    # todo seller_receivable_breakdown
    # todo supplementary_data
    # todo payee
