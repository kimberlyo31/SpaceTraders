class urlbuilder:
  @staticmethod
  def getAuthHeader():
    token = open("agent_token","r")
    return {"Authorization": "Bearer " + token.readline().strip()}