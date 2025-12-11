from .base_api import BaseClient

class AgentClient(BaseClient):
  def get_my_agent(self):
    return self.get("/my/agent")
  
  def get_agent_events(self):
    return self.get("/my/agent/events")