from dataclasses import dataclass
from enums import TradeGood

class Item:
  symbol: TradeGood
  name: str
  description: str
  units: int
  
  def from_json(payload):
    return Item(
      symbol=TradeGood(payload["symbol"]),
      name=payload["name"],
      description=payload["description"],
      units=payload["units"]
    )