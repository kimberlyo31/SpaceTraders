from dataclasses import dataclass
from .modelhelper import serialize
from .market import TradeGood
from src.enums import Deposits, EngineSymbol, FlightMode, FrameSymbol, ModuleSymbol, MountSymbol, ReactorSymbol, ShipRole, CrewRotation, ShipStatus, WaypointType
from enum import Enum


@dataclass
class Cargo:
  capacity: int
  units: int
  inventory: list[TradeGood]
  
  @staticmethod
  def from_json(payload):
    return Cargo(
      capacity=payload["capacity"],
      units=payload["units"],
      inventory=[TradeGood.from_json(item) for item in payload["inventory"]]
    )
  
  def to_json(self):
    return serialize(self)
@dataclass
class Cooldown:
  ship_symbol: str
  total_seconds: int
  remaining_seconds: int
  expiration: str | None = None
  
  def from_json(payload):
    return Cooldown(
      ship_symbol=payload['shipSymbol'],
      total_seconds=payload['totalSeconds'],
      remaining_seconds=payload['remainingSeconds'],
      expiration=payload.get('expiration')
    )
  def to_json(self):
    return serialize(self)
@dataclass
class Crew:
  current: int
  required: int
  capacity: int
  rotation: CrewRotation
  morale: int
  wages: int
   
  @staticmethod 
  def from_json(payload):
    return Crew(
      current=payload["current"],
      required=payload["required"],
      capacity=payload["capacity"],
      rotation=CrewRotation(payload["rotation"]),
      morale=payload["morale"],
      wages=payload["wages"]
    )
  def to_json(self):
    return serialize(self)
@dataclass
class Requirements:
  crew: int
  power: int | None = None
  slots: int | None = None
  
  @staticmethod  
  def from_json(payload):
    return Requirements(
      crew = payload['crew'],
      power = payload.get('power'),
      slots=payload.get('slots')
    )
  def to_json(self):
    return serialize(self)
@dataclass
class Engine:
  symbol: EngineSymbol
  name: str
  condition: float
  integrity: float
  description: str
  speed: int
  requirements: Requirements
  quality: int
    
  @staticmethod
  def from_json(payload):
    return Engine(
      symbol=EngineSymbol(payload['symbol']),
      name=payload['name'],
      condition=payload['condition'],
      integrity=payload['integrity'],
      description=payload['description'],
      speed=payload['speed'],
      requirements=Requirements.from_json(payload['requirements']),
      quality=payload['quality']
    )
  def to_json(self):
    return serialize(self)    
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
    
  @staticmethod
  def from_json(payload):
    return Frame(
      symbol=FrameSymbol(payload['symbol']),
      name=payload['name'],
      condition=payload['condition'],
      integrity=payload['integrity'],
      description=payload['description'],
      module_slots=payload['moduleSlots'],
      mounting_points=payload['mountingPoints'],
      fuel_capacity=payload['fuelCapacity'],
      requirements=Requirements.from_json(payload['requirements']),
      quality=payload['quality']
    )
  def to_json(self):
    return serialize(self)    
@dataclass
class Fuel:
  current: int
  capacity: int
  consumed: int
  timestamp: str
    
  @staticmethod
  def from_json(payload):
    return Fuel(
      current=payload['current'],
      capacity=payload['capacity'],
      consumed=payload['consumed']['amount'],
      timestamp=payload['consumed']['timestamp']
    )
  def to_json(self):
    return serialize(self)    
@dataclass 
class Location:
  symbol: str
  type: WaypointType
  system_symbol: str
  x: int
  y: int
    
  @staticmethod
  def from_json(payload):
    return Location(
      symbol=payload['symbol'],
      type=WaypointType(payload['type']),
      system_symbol=payload['systemSymbol'],
      x=payload['x'],
      y=payload['y']
    )
  def to_json(self):
    return serialize(self)    
@dataclass
class Module:
  symbol: ModuleSymbol
  name: str
  description: str
  requirements: Requirements 
  capacity: int | None = None
  range: int | None = None
    
  @staticmethod
  def from_json(payload):
    return Module(
      symbol=ModuleSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description'],
      requirements=Requirements.from_json(payload['requirements']),
      capacity=payload.get('capacity'),
      range=payload.get('range')
      )
  def to_json(self):
    return serialize(self)    
@dataclass
class Mount:
  symbol: MountSymbol
  name: str
  description: str
  requirements: Requirements 
  strength: int | None = None
  deposits: list[Deposits] | None = None
    
  @staticmethod
  def from_json(payload):
    return Mount(
      symbol=MountSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description'],
      requirements=Requirements.from_json(payload['requirements']),
      strength=payload.get("strength"),
      deposits=[Deposits(d) for d in payload.get("deposits", [])]
      )
  def to_json(self):
    return serialize(self)
@dataclass
class Route:
  destination: Location
  origin: Location
  departure_time: str
  arrival_time: str
    
  @staticmethod
  def from_json(payload):
    return Route(
      destination=Location.from_json(payload['destination']),
      origin=Location.from_json(payload['origin']),
      departure_time=payload['departureTime'],
      arrival_time=payload['arrival']
    )   
  def to_json(self):
    return serialize(self)
@dataclass
class Nav:
  system_symbol: str
  waypoint_symbol: str
  route: Route
  status: ShipStatus
  flight_mode: FlightMode
    
  @staticmethod
  def from_json(payload):
    return Nav(
      system_symbol=payload['systemSymbol'],
      waypoint_symbol=payload['waypointSymbol'],
      route=Route.from_json(payload['route']),
      status=ShipStatus(payload['status']),
      flight_mode=FlightMode(payload['flightMode'])
    )
  def to_json(self):
    return serialize(self)    
@dataclass
class Reactor:
  symbol: ReactorSymbol
  name: str
  condition: float
  integrity: float
  description: str
  power_output: int
  requirements: Requirements
  quality: int
    
  @staticmethod
  def from_json(payload):
    return Reactor(
      symbol=ReactorSymbol(payload['symbol']),
      name=payload['name'],
      condition=payload['condition'],
      integrity=payload['integrity'],
      description=payload['description'],
      power_output=payload['powerOutput'],
      requirements=Requirements.from_json(payload['requirements']),
      quality=payload['quality']
    )
  def to_json(self):
    return serialize(self)    

@dataclass
class Ship:
  symbol: str
  name: str
  faction: str
  role: ShipRole
  nav: Nav
  crew: Crew
  frame: Frame
  reactor: Reactor
  engine: Engine
  modules: list[Module]
  mounts: list[Mount]
  cargo: Cargo
  fuel: Fuel
  cooldown: Cooldown
    
  @staticmethod
  def from_json(payload):
    return Ship(
      symbol=payload['symbol'],
      name=payload['registration']['name'],
      faction=payload['registration']['factionSymbol'],
      role=ShipRole(payload['registration']['role']),
      nav=Nav.from_json(payload['nav']),
      crew=Crew.from_json(payload['crew']),
      frame=Frame.from_json(payload['frame']),
      reactor=Reactor.from_json(payload['reactor']),
      engine=Engine.from_json(payload['engine']),
      modules=[Module.from_json(md) for md in payload["modules"]],
      mounts=[Mount.from_json(mn) for mn in payload["mounts"]],
      cargo=Cargo.from_json(payload['cargo']),
      fuel=Fuel.from_json(payload['fuel']),
      cooldown=Cooldown.from_json(payload['cooldown'])
    )
  def to_json(self):
    return serialize(self)