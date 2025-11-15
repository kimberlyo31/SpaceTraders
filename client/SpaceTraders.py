from AgentClient import AgentClient
from ShipClient import ShipClient

class SpaceTraders:
  def __init__(self,token):
    self.agent = AgentClient(token)
    self.ship = ShipClient(token)