from dataclasses import dataclass
from location import Location
from route import Route
from enums import ShipStatus, FlightMode

@dataclass
class Nav:
  system_symbol: str
  waypoint_symbol: str
  route: Route
  status: ShipStatus
  flight_mode: FlightMode
  
  def from_json(payload):
    return Nav(
      system_symbol=payload['systemSymbol'],
      waypoint_symbol=payload['waypointSymbol'],
      route=Route(payload['route']),
      status=ShipStatus(payload['status']),
      flight_mode=FlightMode(payload['flightMode'])
    )