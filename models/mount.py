from dataclasses import dataclass
from enums import MountSymbol,Deposits
from models.requirements import Requirements

@dataclass
class Mount:
  symbol: MountSymbol
  name: str
  description: str
  requirements: Requirements 
  strength: int | None = None
  deposits: list[Deposits] | None = None
  
  def from_json(payload):
    return Mount(
      symbol=payload['symbol'],
      name=payload['name'],
      description=payload['description'],
      requirements=Requirements.from_json(payload['requirements']),
      strength=payload.get("strength"),
      deposits=[Deposits(d) for d in payload.get("deposits", [])]
      )