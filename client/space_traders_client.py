from api.agent_api import AgentAPI
from api.ship_api import ShipAPI

class SpaceTraders:
  def __init__(self,token):
    self.agent = AgentAPI(token)
    self.ship = ShipAPI(token)