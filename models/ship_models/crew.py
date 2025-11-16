from dataclasses import dataclass
from enums import CrewRotation

@dataclass
class Crew:
  current: int
  required: int
  capacity: int
  rotation: CrewRotation
  morale: int
  wages: int
  
  def from_json(payload):
    return Crew(
      current=payload["current"],
      required=payload["required"],
      capacity=payload["capacity"],
      rotation=CrewRotation(payload["rotation"]),
      morale=payload["morale"],
      wages=payload["wages"]
    )
  