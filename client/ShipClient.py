from BaseClient import BaseClient

class ShipClient(BaseClient):
  
  def list_ships(self):
    return self.get("/my/ships")
  
  def get_ship(self, ship_symbol):
    return self.get(f"my/ships/{ship_symbol}")
  
  def create_chart(self, ship_symbol):
    return self.post(f"my/ships/{ship_symbol}/chart")
  
  def dock_ship(self, ship_symbol):
    return self.post(f"my/ships/{ship_symbol}/dock")
  
  def extract_resources(self, ship_symbol):
    return self.post(f"my/ships/{ship_symbol}/extract")
  
  def navigate_ship(self, ship_symbol, waypoint):
    return self.post(f"my/ships/{ship_symbol}/navigate",{"waypointSymbol":waypoint})