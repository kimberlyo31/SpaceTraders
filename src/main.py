from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from client.space_traders_client import SpaceTraders

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
token = open("agent_token","r").readline().strip()
st = SpaceTraders(token)

# agent = st.agent.get_my_agent()
# print(st.agent.get_my_agent())
@app.get("/api/ships")
def get_ships():
    return st.ship.list_ships()

@app.get("/api/contracts")
def get_contracts():
    return st.agent.get_my_agent()

@app.get("/api/refresh")
def refresh_data():
    return {"ships": st.ship.list_ships(), "contracts": st.agent.get_my_agent()}