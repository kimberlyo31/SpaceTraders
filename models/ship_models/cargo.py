from dataclasses import dataclass
from enums import TradeGood, Item

class Cargo:
  capacity: int
  units: int
  inventory: list[Item]
  
  def from_json(payload):
    return Cargo(
      capacity=payload["capacity"],
      units=payload["units"],
      inventory=[Item.from_json(item) for item in payload["inventory"]]
    )