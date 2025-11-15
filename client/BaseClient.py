import httpx

class BaseClient:
  def __init__(self, token: str):
    self.baseUrl = 'https://api.spacetraders.io/v2'
    self.session = httpx.Client(
      headers={"Authorization": f"Bearer {token}","Content-Type": "application/json"}
    )
    
  def _handle(self,response):
    return response.json()["data"]
  
  def get(self, path):
        res = self.session.get(self.baseUrl + path)
        return self._handle(res)
  
  def post(self, path, payload={}):
    res = self.session.post(self.baseUrl + path, json=payload)
    return self._handle(res)