from dataclasses import dataclass

@dataclass
class Fuel:
  current: int
  capacity: int
  consumed: int
  timestamp: str
  
  def from_json(payload):
    return Fuel(
      current=payload['current'],
      capacity=payload['capacity'],
      consumed=payload['consumed']['amount'],
      timestamp=payload['consumed']['timestamp']
    )