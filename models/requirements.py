from dataclasses import dataclass

@dataclass
class Requirements:
  power: int
  crew: int
  slots: int
  
  def from_json(payload):
    return Requirements(
      power = payload['power'],
      crew = payload['crew'],
      slots=payload['slots']
    )