import datetime as dt

from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

class TradeDetails(BaseModel):
    buySellIndicator: str
    price: float
    quantity: int

class Trade(BaseModel):
    asset_class: Optional[str] = None
    counterparty: Optional[str] = None
    instrument_id: str
    instrument_name: str
    trade_date_time: dt.datetime
    trade_details: TradeDetails
    trade_id: Optional[str] = None
    trader: str

app = FastAPI()

trades = [
    {
        "asset_class": "Equity",
        "counterparty": "Goldman Sachs",
        "instrument_id": "AAPL",
        "instrument_name": "Apple Inc.",
        "trade_date_time": "2022-06-06T18:31:01.000Z",
        "trade_details": {
            "buySellIndicator": "BUY",
            "price": 150.0,
            "quantity": 1000,
        },
        "trade_id": "12345",
        "trader": "John Smith",
    },
    {
        "asset_class": "Bond",
        "counterparty": "JP Morgan",
        "instrument_id": "GOOG",
        "instrument_name": "Alphabet Inc.",
        "trade_date_time": "2022-06-05T18:31:01.000Z",
        "trade_details": {
            "buySellIndicator": "SELL",
            "price": 200.0,
            "quantity": 500,
        },
        "trade_id": "67890",
        "trader": "Jane Doe",
    },
]

@app.get("/trades")
async def get_trades(
    counterparty: Optional[str] = None,
    instrument_id: Optional[str] = None,
    instrument_name: Optional[str] = None,
    trader: Optional[str] = None,
):
    results = []
    for trade in trades:
        if (
            (counterparty is None or trade["counterparty"] == counterparty)
            and (instrument_id is None or trade["instrument_id"] == instrument_id)
            and (instrument_name is None or trade["instrument_name"] == instrument_name)
            and (trader is None or trade["trader"] == trader)
        ):
            results.append(trade)
    return results

