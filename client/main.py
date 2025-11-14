from SpaceTraders import SpaceTraders
from AgentWrapper import AgentWrapper

if __name__ == '__main__':
  token = open("agent_token","r").readline().strip()
  st = SpaceTraders(token)
  payload = st.agent.get_my_agent()
  a = AgentWrapper(payload)
  print(a.symbol)
  
    
    
