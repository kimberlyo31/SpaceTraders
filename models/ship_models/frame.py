from dataclasses import dataclass
from models.requirements import Requirements
from enums import FrameSymbol

@dataclass
class Frame:
  symbol: FrameSymbol
  name: str
  condition: float
  integrity: float
  description: str
  module_slots: int
  mounting_points: int
  fuel_capacity: int
  requirements: Requirements
  quality: int
  
  def from_json(payload):
    return Frame(
      symbol=FrameSymbol(payload['symbol']),
      name=payload['name'],
      condition=payload['float'],
      integrity=payload['integrity'],
      description=payload['description'],
      module_slots=payload['moduleSlots'],
      mounting_points=payload['mountingPoints'],
      fuel_capacity=payload['fuelCapacity'],
      requirements=Requirements.from_json(payload['requirements']),
      quality=payload['quality']
    )