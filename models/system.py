from dataclasses import dataclass
from enums import SystemType, WaypointType, WaypointModifierSymbol, WaypointTraitSymbol
from faction import Faction

@dataclass
class WaypointOrbital:
  symbol: str
  
  def from_json(payload):
    return WaypointOrbital()

@dataclass
class WaypointModifier:
  symbol: WaypointModifierSymbol
  name: str
  description: str
  
  def from_json(payload):
    return WaypointTrait(
      symbol=WaypointModifierSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description']
    )
  
@dataclass
class WaypointTrait:
  symbol: WaypointTraitSymbol
  name: str
  description: str
  
  def from_json(payload):
    return WaypointTrait(
      symbol=WaypointTraitSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description']
    )
  
@dataclass
class Waypoint:
  symbol: str
  type: WaypointType
  x: int
  y: int
  orbitals: list[WaypointOrbital]
  orbits: str
  def from_json(payload):
    return Waypoint()
  
@dataclass
class System:
  contsellation: str
  symbol: str
  sector_symbol: str
  type: SystemType
  x: int
  y: int
  waypoints: list[Waypoint]
  factions: list[Faction]
  name: str
  
  def from_json(payload):
    return System()