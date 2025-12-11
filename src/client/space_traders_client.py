from src.api.agent_api import AgentClient
from src.api.ship_api import ShipClient
from src.api.contract_api import ContractClient

class SpaceTraders:
  def __init__(self,token):
    self.agent = AgentClient(token)
    self.ship = ShipClient(token)
    self.contract = ContractClient(token)