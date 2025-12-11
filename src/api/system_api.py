from .base_api import BaseClient

class SystemClient(BaseClient):
  
  def list_systems(self):
    return self.get("/systems")
  
  def get_system(self, system_symbol):
    return self.get(f"/systems/{system_symbol}")
  
  def list_waypoints_in_system(self, system_symbol):
    return self.get(f"/systems/{system_symbol}/waypoints")
  
  def get_waypoint(self, system_symbol, waypoint_symbol):
    return self.get(f"/systems/{system_symbol}/waypoints/{waypoint_symbol}")
  
  def get_construction_site(self, system_symbol, waypoint_symbol):
    return self.get(f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/construction")
  
  def supply_construction_site(self, system_symbol, waypoint_symbol, ship_symbol, trade_symbol, units):
    p = {"shipSymbol":ship_symbol, "tradeSymbol":trade_symbol, "units":units}
    return self.post(f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/construction/supply",p)
  
  def get_market(self, system_symbol, waypoint_symbol):
    return self.get(f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/market")
  
  def get_jump_gate(self, system_symbol, waypoint_symbol):
    return self.get(f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/jump-gate")
  
  def get_shipyard(self, system_symbol, waypoint_symbol):
    return self.get(f"/systems/{system_symbol}/waypoints/{waypoint_symbol}/shipyard")