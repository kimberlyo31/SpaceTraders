from dataclasses import dataclass

@dataclass
class Agent:
  accountId: str
  symbol: str
  headquarters: str
  credits: int
  starting_faction: str
  ship_count: int
  
  @staticmethod
  def from_json(payload):
    return Agent(
      accountId=payload['accountId'],
      symbol=payload['symbol'],
      headquarters=payload['headquarters'],
      credits=payload['credits'],
      starting_faction=payload['startingFaction'],
      ship_count=payload['shipCount']
    )