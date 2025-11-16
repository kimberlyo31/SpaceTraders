from dataclasses import dataclass
from enums import WaypointType

@dataclass 
class Location:
  symbol: str
  type: WaypointType
  system_symbol: str
  x: int
  y: int
  
  def from_json(payload):
    return Location(
      symbol=payload['symbol'],
      type=WaypointType(payload['type']),
      system_symbol=payload['systemSymbol'],
      x=payload['x'],
      y=payload['y']
    )