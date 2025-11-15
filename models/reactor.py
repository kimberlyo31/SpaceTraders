from dataclasses import dataclass

@dataclass
class Reactor:
  symbol: str
  name: str
  condition: float
  integrity: float
  description: str
  power_output: int
  req_power: int
  req_crew: int
  req_slots: int
  quality: int
  
  def from_json(payload):
    return Reactor(
      symbol=payload['symbol'],
      name=payload['name'],
      condition=payload['float'],
      integrity=payload['integrity'],
      description=payload['description'],
      power_output=payload['powerOutput'],
      req_power=payload['requirements']['power'],
      req_crew=payload['requirements']['crew'],
      req_slots=payload['requirements']['slots'],
      quality=payload['quality']
    )
