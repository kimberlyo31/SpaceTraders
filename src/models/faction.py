from dataclasses import dataclass
from enums import FactionSymbol, FactionTraitSymbol
from .modelhelper import mserialize
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
  def to_json(self):
    return mserialize(self)    
@dataclass
class Faction:
  symbol: FactionSymbol
  name: str
  description: str
  headquarters: str
  traits: list[FactionTrait]
  is_recruiting: bool
  
  def from_json(payload: dict):
    return Faction(
      symbol=FactionSymbol(payload.get('symbol')),
      name=payload.get('name'),
      description=payload.get('description'),
      headquarters=payload.get('headquarters'),
      traits=[FactionTrait.from_json(f) for f in payload.get('traits')]if payload.get('faction') else None,
      is_recruiting=payload.get('is_recruiting'),
    )
  def to_json(self):
    return mserialize(self)