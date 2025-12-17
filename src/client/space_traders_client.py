from api.agent_api import AgentClient
from api.ship_api import ShipClient
from api.contract_api import ContractClient
from api.system_api import SystemClient

class SpaceTraders:
  def __init__(self,token):
    self.agent = AgentClient(token)
    self.ship = ShipClient(token)
    self.contract = ContractClient(token)
    self.systems = SystemClient(token)