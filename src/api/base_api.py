import httpx
from .errors import ShipCooldownError

class BaseClient:
  def __init__(self, token: str):
    self.baseUrl = 'https://api.spacetraders.io/v2'
    self.session = httpx.Client(
      headers={"Authorization": f"Bearer {token}","Content-Type": "application/json"}
    )
    
  def _handle(self, response):
    json_resp = response.json()
    if "error" in json_resp:
        if "cooldown" in json_resp["error"]["data"]:
            raise ShipCooldownError(json_resp["error"]["data"]["cooldown"])
        else:
            raise Exception(json_resp["error"]["message"])
    return json_resp.get("data", json_resp)
  
  def get(self, path):
        res = self.session.get(self.baseUrl + path)
        return self._handle(res)
  
  def post(self, path, payload={}):
    res = self.session.post(self.baseUrl + path, json=payload)
    return self._handle(res)
  
  def patch(self, path, payload={}):
    res = self.session.patch(self.baseUrl + path, json=payload)
    return self._handle(res)