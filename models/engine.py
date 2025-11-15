from dataclasses import dataclass

@dataclass
class Engine:
  symbol: str
  name: str
  condition: float
  integrity: float
  description: str
  speed: int
  req_power: int
  req_crew: int
  req_slots: int
  quality: int
  
  def from_json(payload):
    return Engine(
      symbol=payload['symbol'],
      name=payload['name'],
      condition=payload['float'],
      integrity=payload['integrity'],
      description=payload['description'],
      speed=payload['speed'],
      req_power=payload['requirements']['power'],
      req_crew=payload['requirements']['crew'],
      req_slots=payload['requirements']['slots'],
      quality=payload['quality']
    )