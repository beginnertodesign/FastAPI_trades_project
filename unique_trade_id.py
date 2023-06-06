import datetime as dt

from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")

trades = [
    {
        "asset_class": "Equity",
        "counterparty": "Goldman Sachs",
        "instrument_id": "ABCD",
        "instrument_name": "Apple",
        "trade_date_time": "2022-06-06T18:31:01.000Z",
        "trade_details": {
            "buySellIndicator": "BUY",
            "price": 100.0,
            "quantity": 100,
        },
        "trade_id": "12345",
        "trader": "John Smith",
    },
    {
        "asset_class": "Bond",
        "counterparty": "JP Morgan",
        "instrument_id": "EFGH",
        "instrument_name": "Alphabet Inc.",
        "trade_date_time": "2022-06-05T18:31:01.000Z",
        "trade_details": {
            "buySellIndicator": "SELL",
            "price": 200.0,
            "quantity": 50,
        },
        "trade_id": "67890",
        "trader": "Jane Doe",
    },
]

@app.get("/trades/{trade_id}")
async def get_trade_by_id(trade_id: str):
    for trade in trades:
        if trade["trade_id"] == trade_id:
            return trade
    return {"error": f"Trade with id {trade_id} not found"}


