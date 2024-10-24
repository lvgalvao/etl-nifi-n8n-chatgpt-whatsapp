from sqlmodel import SQLModel, Field

class BitcoinPrice(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: float
    base: str
    currency: str
