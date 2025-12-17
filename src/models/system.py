from dataclasses import dataclass
from enums import SystemType, WaypointType, WaypointModifierSymbol, WaypointTraitSymbol
from .faction import Faction
from .agent import Agent
from .modelhelper import mserialize

@dataclass
class WaypointOrbital:
  symbol: str
  
  @staticmethod
  def from_json(payload: dict):
    return WaypointOrbital(
      symbol=payload['symbol']
    )
  def to_json(self):
    return mserialize(self)
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
  def to_json(self):
    return mserialize(self)  
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
  def to_json(self):
    return mserialize(self)  
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
  def to_json(self):
    return mserialize(self)    
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
      waypoint_type=WaypointType(payload['type']),
      system_symbol="-".join(payload['symbol'].split("-")[:2]),
      x=payload['x'],
      y=payload['y'],
      orbitals=[WaypointOrbital.from_json(o) for o in payload.get('orbitals', [])],
      traits=[WaypointTrait.from_json(t) for t in payload.get('traits', [])],
      isUnderConstruction=payload.get('isUnderConstruction'),
      orbits=payload.get('orbits'),
      faction = Faction.from_json(payload['faction']) if payload.get('faction') else None,
      modifiers=[WaypointTrait.from_json(m) for m in payload.get('modifiers', [])],
      chart=Chart.from_json(payload.get('chart'))if payload.get('chart') else None
    )
  def to_json(self):
    return mserialize(self)  
@dataclass
class System:
  symbol: str
  sector_symbol: str
  system_type: SystemType
  x: int
  y: int
  waypoints: list[Waypoint]
  factions: list[Faction]
  constellation: str | None = None
  name: str | None = None
  
  @staticmethod
  def from_json(payload: dict) -> "System":
    return System(
      symbol=payload["symbol"],
      sector_symbol=payload["sectorSymbol"],
      system_type=SystemType(payload["type"]),
      x=payload["x"],
      y=payload["y"],
      waypoints=[Waypoint.from_json(wp) for wp in payload["waypoints"]],
      factions=[Faction.from_json(f) for f in payload.get("factions", [])],
      constellation=payload["constellation"],
      name=payload["name"]
    )
  def to_json(self):
    return mserialize(self)