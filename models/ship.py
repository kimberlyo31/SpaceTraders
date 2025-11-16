from dataclasses import dataclass
from enums import ShipRole
from nav import Nav
from crew import Crew
from frame import Frame
from reactor import Reactor
from engine import Engine
from module import Module
from mount import Mount
from cargo import Cargo
from fuel import Fuel
from cooldown import Cooldown

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
      mounts=[Module.from_json(mn) for mn in payload["mounts"]],
      cargo=Cargo.from_json(payload['cargo']),
      fuel=Fuel.from_json(payload['fuel']),
      cooldown=Cooldown.from_json(payload['cooldown'])
    )