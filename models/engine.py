from dataclasses import dataclass
from models.requirements import Requirements
@dataclass
class Engine:
  symbol: str
  name: str
  condition: float
  integrity: float
  description: str
  speed: int
  requirements: Requirements
  quality: int
  
  def from_json(payload):
    return Engine(
      symbol=payload['symbol'],
      name=payload['name'],
      condition=payload['float'],
      integrity=payload['integrity'],
      description=payload['description'],
      speed=payload['speed'],
      requirements=Requirements.from_json(payload['requirements']),
      quality=payload['quality']
    )