from .base_api import BaseClient

class ShipClient(BaseClient):
  
  def list_ships(self):
    return self.get("/my/ships")
  
  def purchase_ship(self, ship_type, waypoint_symbol):
    p = {"shipType":ship_type,"waypointSymbol":waypoint_symbol}
    return self.post("/my/ships", p)
  
  def get_ship(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}")
  
  def create_chart(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/chart")
  
  def negotiate_contract(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/negotiate/contract")
  
  def ship_cooldown(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/cooldown")
  
  def dock_ship(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/dock")
  
  def extract_resources(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/extract")
  
  def extract_resources_survey(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/extract/survey")
  
  def jettison_cargo(self, ship_symbol, goods_symbol, units):
    p = {"symbol":goods_symbol, "units":units}
    return self.post(f"/my/ships/{ship_symbol}/jettison",p)
  
  def jump_ship(self, ship_symbol, waypoint):
    p = {"waypointSymbol":waypoint}
    return self.post(f"/my/ships/{ship_symbol}/jump", p)
  
  def scan_systems(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/scan/systems")
  
  def scan_waypoints(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/scan/waypoints")
  
  def scan_ships(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/scan/ships")
  
  def scrap_ship(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/scrap")
  
  def get_scrap_value(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/scrap")
  
  def navigate_ship(self, ship_symbol, waypoint):
    p = {"waypointSymbol":waypoint}
    return self.post(f"/my/ships/{ship_symbol}/navigate", p)
  
  def warp_ship(self, ship_symbol, waypoint):
    p = {"waypointSymbol":waypoint}
    return self.post(f"/my/ships/{ship_symbol}/warp", p)
  
  def orbit_ship(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/orbit")
  
  def purchase_cargo(self, ship_symbol, goods_symbol, units):
    p = {"symbol":goods_symbol, "units":units}
    return self.post(f"/my/ships/{ship_symbol}/purchase", p)
  
  def ship_refine(self, ship_symbol, produce):
    p = {"produce":produce}
    return self.post(f"/my/ships/{ship_symbol}/refine", p)
  
  def refuel_ship(self, ship_symbol, units, from_cargo):
    p = {"units":units, "fromCargo":from_cargo}
    return self.post(f"/my/ships/{ship_symbol}/refuel", p)
  
  def repair_ship(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/repair")
  
  def get_repair_value(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/repair")
  
  def sell_cargo(self, ship_symbol, goods_symbol, units):
    p = {"symbol":goods_symbol, "units":units}
    return self.post(f"/my/ships/{ship_symbol}/sell", p)
  
  def siphon_resources(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/siphon")
  
  def create_survey(self, ship_symbol):
    return self.post(f"/my/ships/{ship_symbol}/survey")
  
  def transfer_cargo(self, ship_symbol, trade_symbol, units, to_ship_symbol):
    p = {"tradeSymbol":trade_symbol, "units":units, "shipSymbol": to_ship_symbol}
    return self.post(f"/my/ships/{ship_symbol}/sell", p)
  
  def get_ship_cargo(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/cargo")
  
  def get_ship_modules(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/modules")
  
  def install_ship_module(self, ship_symbol, module_symbol):
    p = {"symbol":module_symbol}
    return self.post(f"/my/ships/{ship_symbol}/modules/install", p)
  
  def remove_ship_module(self, ship_symbol, module_symbol):
    p = {"symbol":module_symbol}
    return self.post(f"/my/ships/{ship_symbol}/modules/remove", p)
  
  def get_mounts(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/mounts")
  
  def install_mount(self, ship_symbol, mount_symbol):
    p = {"symbol":mount_symbol}
    return self.post(f"/my/ships/{ship_symbol}/mounts/install", p)
  
  def remove_mount(self, ship_symbol, mount_symbol):
    p = {"symbol":mount_symbol}
    return self.post(f"/my/ships/{ship_symbol}/mounts/remove", p)
  
  def get_ship_nav(self, ship_symbol):
    return self.get(f"/my/ships/{ship_symbol}/nav")
  
  def patch_ship_nav(self, ship_symbol, flight_mode):
    p = {"flightMode":flight_mode}
    return self.patch(f"/my/ships/{ship_symbol}/nav", p)