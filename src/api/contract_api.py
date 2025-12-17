from .base_api import BaseClient

class ContractClient(BaseClient):
  
  def list_contracts(self):
    return self.get("/my/contracts")
  
  def get_contract(self, contract_id):
    return self.get(f"/my/contracts/{contract_id}")
  
  def accept_contract(self, contract_id):
    return self.post(f"/my/contracts/{contract_id}/accept")
  
  def fulfill_contract(self, contract_id):
    return self.post(f"/my/contracts/{contract_id}/fulfill")
  
  def deliver_cargo_contract(self, contract_id,ship_symbol,trade_symbol,units):
    p = {"shipSymbol":ship_symbol, "tradeSymbol":trade_symbol, "units": units}
    return self.post(f"/my/contracts/{contract_id}/deliver",p)
  
  def negotiate_contract(self, ship_symbol):
    return self.post(f"/my/contracts/{ship_symbol}/negotiate/contract")