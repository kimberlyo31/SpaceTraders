from dataclasses import dataclass
from enums import TradeGoodSymbol

class TradeGood:
  symbol: TradeGoodSymbol
  name: str
  description: str
  units: int
  
  def from_json(payload):
    return TradeGood(
      symbol=TradeGoodSymbol(payload["symbol"]),
      name=payload["name"],
      description=payload["description"],
      units=payload["units"]
    )