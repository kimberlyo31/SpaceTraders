from dataclasses import dataclass
from src.enums import TradeGoodSymbol
from .modelhelper import mserialize
@dataclass
class ConstructionMaterial:
  trade_symbol: TradeGoodSymbol
  required: int
  fulfilled: int
  
  @staticmethod
  def from_json(payload):
    return ConstructionMaterial(
      trade_symbol=TradeGoodSymbol(payload['tradeSymbol']),
      required=payload['required'],
      fulfilled=payload['fulfilled']
    )
  def to_json(self):
    return mserialize(self)    
@dataclass
class Construction:
  symbol: str
  materials: list[ConstructionMaterial]
  is_complete: bool
  
  @staticmethod
  def from_json(payload):
    return Construction(
      symbol=payload['symbol'],
      materials=[ConstructionMaterial.from_json(item) for item in payload["materials"]],
      is_complete=payload['isComplete']
    )
  def to_json(self):
    return mserialize(self)