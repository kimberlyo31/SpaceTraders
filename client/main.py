import requests
import json
import sys
from PySide6.QtWidgets import *
import ship

if __name__ == '__main__':
    # response = requests.get('https://api.spacetraders.io/v2')
    # print(json.dumps(response.json(), indent=2))
    # app = QApplication(sys.argv)
    # label = QLabel("Hello")
    # label.show()
    # sys.exit(app.exec())
    ship.Ship.getCargo("GR1M-3")
