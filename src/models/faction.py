from dataclasses import dataclass
from src.enums import FactionSymbol, FactionTraitSymbol
@dataclass
class FactionTrait:
  symbol: FactionTraitSymbol
  name: str
  description: str
  
  def from_json(payload):
    return FactionTrait(
      symbol=FactionTraitSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description']
    )
    
@dataclass
class Faction:
  symbol: FactionSymbol
  name: str
  description: str
  headquarters: str
  traits: list[FactionTrait]
  is_recruiting: bool
  
  def from_json(payload):
    return Faction(
      symbol=FactionSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description'],
      headquarters=payload['headquarters'],
      traits=[FactionTrait.from_json(f) for f in payload["traits"]],
      is_recruiting=payload['is_recruiting'],
    )