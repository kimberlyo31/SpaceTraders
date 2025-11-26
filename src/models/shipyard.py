from dataclasses import dataclass
from src.enums import ShipType, Activity, Supply
from ship import Frame, Reactor, Engine, Module, Mount, Crew


@dataclass
class ShipyardShip:
  type: ShipType
  name: str
  description: str
  supply: Supply
  purchase_price: int
  frame: Frame
  reactor: Reactor
  engine: Engine
  modules: list[Module]
  mounts: list[Mount]
  crew: Crew
  activity: Activity | None = None
  
  @staticmethod
  def from_json(payload):
    return ShipyardShip(
      type=ShipType(payload['type']),
      name=payload['name'],
      description=payload['description'],
      supply=Supply(payload['supply']),
      purchase_price=payload['purchasePrice'],
      frame=Frame(payload['frame']),
      reactor=Reactor(payload['reactor']),
      engine=Engine(payload['engine']),
      modules=[Module.from_json(item) for item in payload["modules"]],
      mounts=[Mount.from_json(item) for item in payload["mounts"]],
      crew=Crew(payload['crew']),
      activity=payload.get('activity')
    )

@dataclass
class ShipyardTransaction:
  waypoint_symbol: str
  ship_type: ShipType
  price: int
  agent_symbol: str
  timestamp: str
  
  @staticmethod
  def from_json(payload):
    return ShipyardTransaction(
      waypoint_symbol=payload['waypointSymbol'],
      ship_type=payload['shipType'],
      price=payload['price'],
      agent_symbol=payload['agentSymbol'],
      timestamp=payload['timestamp']
    )
    
@dataclass
class Shipyard:
  symbol: str
  ship_types: list[ShipType]
  transactions: list[ShipyardTransaction]
  ships: list[ShipyardShip]
  modifications_fee: int
  
  @staticmethod
  def from_json(payload):
    return Shipyard(
      symbol=payload['symbol'],
      ship_types=[ShipType(item) for item in payload["shipTypes"]],
      transactions=[ShipyardTransaction.from_json(item) for item in payload["transactions"]],
      ships=[ShipyardShip.from_json(item) for item in payload["ships"]],
      modifications_fee=payload['modificationsFee']
    )