from dataclasses import dataclass
from models.requirements import Requirements
from enums import ReactorSymbol

@dataclass
class Reactor:
  symbol: ReactorSymbol
  name: str
  condition: float
  integrity: float
  description: str
  power_output: int
  requirements: Requirements
  quality: int
  
  def from_json(payload):
    return Reactor(
      symbol=ReactorSymbol(payload['symbol']),
      name=payload['name'],
      condition=payload['float'],
      integrity=payload['integrity'],
      description=payload['description'],
      power_output=payload['powerOutput'],
      requirements=Requirements.from_json(payload['requirements']),
      quality=payload['quality']
    )
