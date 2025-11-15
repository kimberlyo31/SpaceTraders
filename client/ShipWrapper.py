import json

class ShipWrapper:
  def __init__(self, payload):
    self.symbol = payload['symbol']
    self.role = payload['registration']['role']
    
    #navigation
    self.system_symbol = payload['nav']['systemSymbol']
    self.waypoint_symbol = payload['nav']['waypointSymbol']
    self.depature_time = payload['nav']['departureTime']
    self.arrival = payload['nav']['arrival']
    #route
    self.des_symbol = payload['nav']['route']['destination']['symbol']
    self.des_type = payload['nav']['route']['destination']['type']
    self.des_system_symbol = payload['nav']['route']['destination']['systemSymbol']
    self.des_x = payload['nav']['route']['destination']['x']
    self.des_y = payload['nav']['route']['destination']['y']
    #origin
    self.or_symbol = payload['nav']['route']['origin']['symbol']
    self.or_type = payload['nav']['route']['origin']['type']
    self.or_system_symbol = payload['nav']['route']['origin']['systemSymbol']
    self.or_x = payload['nav']['route']['origin']['x']
    self.or_y = payload['nav']['route']['origin']['y']
    
    #crew
    self.c_current = payload['crew']['current']
    self.c_required = payload['crew']['required']
    self.c_capacity = payload['crew']['capacity']
    self.c_rotation = payload['crew']['rotation']
    self.c_morale = payload['crew']['morale']
    self.c_wages = payload['crew']['wages']
    
    #frame
    self.f_symbol = payload['frame']['symbol']
    self.f_name = payload['frame']['name']
    self.f_condition = payload['frame']['condition']
    self.f_integrity = payload['frame']['integrity']
    self.f_desc = payload['frame']['description']
    self.f_module_slots = payload['frame']['moduleSlots']
    self.f_mounting_points = payload['frame']['mountingPoints']
    self.f_fuel_capacity = payload['frame']['fuelCapacity']
    self.f_req_power = payload['frame']['requirements']['power']
    self.f_req_crew = payload['frame']['requirements']['crew']
    self.f_req_slots = payload['frame']['requirements']['slots']
    self.f_quality = payload['frame']['quality']
    
    
    