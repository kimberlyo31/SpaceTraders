from dataclasses import dataclass

@dataclass
class Cooldown:
  ship_symbol: str
  total_seconds: int
  remaining_seconds: int
  expiration: str
  
  def from_json(payload):
    return Cooldown(
      ship_symbol=payload['shipSymbol'],
      total_seconds=payload['totalSeconds'],
      remaining_seconds=payload['remainingSeconds'],
      expiration=payload['expiration']
    )