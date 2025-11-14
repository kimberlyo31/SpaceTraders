from SpaceTraders import SpaceTraders

if __name__ == '__main__':
  token = open("agent_token","r").readline().strip()
  st = SpaceTraders(token)
  print(st.agent.get_my_agent())
  
    
    
