from dataclasses import dataclass
from src.enums import SystemType, WaypointType, WaypointModifierSymbol, WaypointTraitSymbol
from faction import Faction
from agent import Agent

@dataclass
class WaypointOrbital:
  symbol: str
  
  @staticmethod
  def from_json(payload: dict):
    return WaypointOrbital(
      symbol=payload['symbol']
    )

@dataclass
class WaypointModifier:
  symbol: WaypointModifierSymbol
  name: str
  description: str
  
  @staticmethod
  def from_json(payload: dict):
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
  
  @staticmethod
  def from_json(payload: dict):
    return WaypointTrait(
      symbol=WaypointTraitSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description']
    )
  
@dataclass
class Chart:
  waypoint_symbol: str
  submitted_by: Agent
  submitted_on: str
  
  @staticmethod
  def from_json(payload: dict):
    return Chart(
      waypoint_symbol=payload['waypointSymbol'],
      submitted_by=Agent(payload['submittedBy']),
      submitted_on=payload['submittedOn']
    )
@dataclass
class Waypoint:
  symbol: str
  waypoint_type: WaypointType
  system_symbol: str
  x: int
  y: int
  orbitals: list[WaypointOrbital]
  traits: list[WaypointTrait]
  isUnderConstruction: bool
  orbits: str | None = None
  faction: Faction | None = None
  modifiers: list[WaypointModifier] | None = None
  chart: Chart | None = None
  
  @staticmethod
  def from_json(payload: dict):
    return Waypoint(
      symbol=payload['symbol'],
      type=WaypointType(payload['type']),
      system_symbol=payload['systemSymbol'],
      x=payload['x'],
      y=payload['y'],
      orbitals=[WaypointOrbital.from_json(o) for o in payload['orbitals']],
      traits=[WaypointTrait.from_json(t) for t in payload['traits']],
      isUnderConstruction=payload['isUnderConstruction'],
      orbits=payload['orbits'],
      faction=Faction.from_json(payload['faction']),
      modifiers=[WaypointTrait.from_json(m) for m in payload['modifiers']],
      chart=Chart.from_json(payload['chart'])
    )
  
@dataclass
class System:
  symbol: str
  sector_symbol: str
  type: SystemType
  x: int
  y: int
  waypoints: list[Waypoint]
  factions: list[Faction]
  contsellation: str | None = None
  name: str | None = None
  
  @staticmethod
  def from_json(payload: dict) -> "System":
    return System(
      symbol=payload["symbol"],
      sector_symbol=payload["sectorSymbol"],
      type=SystemType(payload["type"]),
      x=payload["x"],
      y=payload["y"],
      waypoints=[Waypoint.from_json(wp) for wp in payload["waypoints"]],
      factions=[Faction.from_json(f) for f in payload.get("factions", [])],
      constellation=payload["constellation"],
      name=payload["name"]
    )