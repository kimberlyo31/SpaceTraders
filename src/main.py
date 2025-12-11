import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.client.space_traders_client import SpaceTraders
from src.models.ship import *
from src.client.db import Database

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
base_dir = os.path.dirname(__file__)
token_path = os.path.join(base_dir, "agent_token")

with open(token_path, "r") as f:
  token = f.readline().strip()
st = SpaceTraders(token)

class ShipRequest(BaseModel):
  symbol: str
  
class WaypointRequest(BaseModel):
  systemSymbol: str
  waypointSymbol: str
# agent = st.agent.get_my_agent()
# print(st.agent.get_my_agent())
@app.get("/api/ships")
def get_ships():
  res = st.ship.get_ship()
  return st.ship.list_ships()

@app.get("/api/contracts")
def get_contracts():
    return st.contract.list_contracts()

@app.get("/api/refresh")
def refresh_data():
    return {"ships": st.ship.list_ships(), "contracts": st.agent.get_my_agent()}

@app.post("/api/orbit")
def orbit_ship(req: ShipRequest):
    result = st.ship.orbit_ship(req.symbol)  # however your client works
    return {"status": "ok", "response": result}
  
@app.post("/api/dock")
def docK_ship(req: ShipRequest):
    result = st.ship.dock_ship(req.symbol)  # however your client works
    return {"status": "ok", "response": result}
  
@app.post("/api/scan")
def scan_system(req: ShipRequest):
    # Example: call your SpaceTraders client
    try:
        result = st.ship.scan_systems(req.symbol)
        print(result)
        print(type(result))
        systems = list(result.values()) if isinstance(result, dict) else []
        return {"status": "ok", "systems": systems}
    except Exception as e:
        # Log the error so you know what went wrong
        print("Error in scan_ship:", e)
        raise
      
if __name__ == "__main__":
  res = st.ship.list_ships()
  db = Database("kospacetraders.sqlite")
  for r in res:
    s = Ship.from_json(r)
    # print(s.nav.to_json())
    db.insert_ship(s)
  db.close() 
