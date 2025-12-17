from dataclasses import dataclass
from .modelhelper import mserialize
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
  def to_json(self):
    return mserialize(self)