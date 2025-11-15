from dataclasses import dataclass

@dataclass
class Frame:
  symbol: str
  name: str
  condition: float
  integrity: float
  description: str
  module_slots: int
  mounting_points: int
  fuel_capacity: int
  req_power: int
  req_crew: int
  req_slots: int
  quality: int
  
  def from_json(payload):
    return Frame(
      symbol=payload['symbol'],
      name=payload['name'],
      condition=payload['float'],
      integrity=payload['integrity'],
      description=payload['description'],
      module_slots=payload['moduleSlots'],
      mounting_points=payload['mountingPoints'],
      fuel_capacity=payload['fuelCapacity'],
      req_power=payload['requirements']['power'],
      req_crew=payload['requirements']['crew'],
      req_slots=payload['requirements']['slots'],
      quality=payload['quality']
    )