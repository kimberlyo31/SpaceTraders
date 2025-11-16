from dataclasses import dataclass
from location import Location

@dataclass
class Route:
  destination: Location
  origin: Location
  departure_time: str
  arrival_time: str
  
  def from_json(payload):
    return Route(
      destination=Location(payload['route']['destination']),
      origin=Location(payload['route']['origin']),
      departure_time=payload['departureTime'],
      arrival_time=payload['arrival']
    )