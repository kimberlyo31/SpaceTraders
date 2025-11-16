from dataclasses import dataclass
from enums import ModuleSymbol
from models.requirements import Requirements

@dataclass
class Module:
  symbol: ModuleSymbol
  name: str
  description: str
  requirements: Requirements 
  capacity: int | None = None
  range: int | None = None
  
  def from_json(payload):
    return Module(
      symbol=payload['symbol'],
      name=payload['name'],
      description=payload['description'],
      requirements=Requirements.from_json(payload['requirements']),
      capacity=payload['capacity'],
      range=payload['range']
      )