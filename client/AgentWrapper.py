import json

class AgentWrapper:
  def __init__(self, payload):
    self.accountid = payload['accountId']
    self.symbol = payload['symbol']
    self.headquarters = payload['headquarters']
    self.credits = payload['credits']
    self.startingFaction = payload['startingFaction']
    self.shipCount = payload['shipCount']
    