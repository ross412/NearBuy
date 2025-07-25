import time
from enum import Enum
from sqlmodel import Column, Integer, SQLModel, Field, func
from typing import Optional

class StockStatus(str, Enum):
    IN_STOCK = "IN_STOCK"
    LOW = "LOW"
    OUT_OF_STOCK = "OUT_OF_STOCK"

class Inventory(SQLModel, table=True):
    shop_id: int = Field(foreign_key="shop.id", primary_key=True)
    item_id: int = Field(foreign_key="item.id", primary_key=True)
    quantity: int = Field(default=0)
    price_at_entry: Optional[float] = Field(default=None)
    last_restocked_at: Optional[int] = Field(default_factory=lambda: int(time.time()))
    min_quantity: Optional[int] = Field(default=5)
    max_quantity: Optional[int] = Field(default=100)
    status: Optional[StockStatus] = Field(default=StockStatus.IN_STOCK)
    location: Optional[str] = Field(default=None)
    batch_number: Optional[str] = Field(default=None)
    expiry_date: Optional[int] = Field(default=None)
    updated_at: Optional[int] = Field(default=None,sa_column=Column(Integer, onupdate=func.extract("epoch", func.now())),)
    note: Optional[str] = Field(default=None)