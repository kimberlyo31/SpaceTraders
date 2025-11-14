import requests
import json
import constants as c
from urlbuilder import urlbuilder as u

class Ship:
    
    @staticmethod  
    def getCargo(ship_symbol):
        # token = open("agent_token","r")
        # headers={"Authorization": "Bearer " + token.readline().strip()}
        response = requests.get(c.baseUrl+'/my/ships/'+ship_symbol+'/cargo', headers=u.getAuthHeader())
        data = response.json()
        inventory = data['data']['inventory']
        for record in inventory:
          print('Item '+record['symbol']+ ' Quantity ' + str(record['units']))
    