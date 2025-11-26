from client.space_traders_client import SpaceTraders
from AgentWrapper import AgentWrapper
import json

if __name__ == '__main__':
  token = open("agent_token","r").readline().strip()
  ship_symbol = "GR1M-3"
  st = SpaceTraders(token)
  data = st.ship.list_ships()
  p = json.dumps(data,indent=2)
  print(p)
  # print(st.ship.extract_resources(ship_symbol))
  
    
    
