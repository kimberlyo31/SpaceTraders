import sqlite3
import json
from typing import List, Tuple, Optional
from models.ship import *
from models.system import *
from models.market import *
from models.modelhelper import *
from enums import *


class Database:
  def __init__(self, db_file: str):
    """Initialize the database connection"""
    self.conn = sqlite3.connect(db_file)
    self.cursor = self.conn.cursor()
    self._create_table()

  def _create_table(self):
    """Create a ship table"""
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS ships (
        symbol TEXT PRIMARY KEY,
        name TEXT,
        faction TEXT,
        role TEXT
      )
    """)
    
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS systems (
        symbol TEXT PRIMARY KEY,
        sector_symbol TEXT NOT NULL,
        type TEXT NOT NULL,
        x INTEGER NOT NULL,
        y INTEGER NOT NULL,
        constellation TEXT,
        name TEXT
      )
    """)
    
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS waypoints (
        symbol TEXT PRIMARY KEY,
        system_symbol TEXT NOT NULL,
        type TEXT NOT NULL,
        x INTEGER NOT NULL,
        y INTEGER NOT NULL,
        FOREIGN KEY (system_symbol) REFERENCES systems(symbol)
      )
    """)
    
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS factions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        system_symbol TEXT,
        waypoint_symbol TEXT,
        name TEXT,
        symbol TEXT,
        FOREIGN KEY (system_symbol) REFERENCES systems(symbol),
        FOREIGN KEY (waypoint_symbol) REFERENCES waypoints(symbol)
      )
    """)
    self.conn.commit()

  def insert_waypoints(self, waypoint: Waypoint):
    self.cursor.execute("""
        INSERT OR REPLACE INTO waypoints (
          symbol, system_symbol, type, x, y
        ) VALUES (?, ?, ?, ?, ?)
      """, (
        waypoint.symbol, waypoint.system_symbol, waypoint.waypoint_type.value, waypoint.x, waypoint.y
      ))

  # ---------------- Get Waypoints ----------------
  def get_waypoints(self):
    self.cursor.execute("SELECT symbol FROM waypoints")
    return [row[0] for row in self.cursor.fetchall()]
      
  def insert_system(self, system: System):
    self.cursor.execute("""
      INSERT OR REPLACE INTO systems (symbol, sector_symbol, type, x, y, constellation, name)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (system.symbol, system.sector_symbol, system.system_type.value, system.x, system.y, system.constellation, system.name))


    for wp in system.waypoints:
      self.insert_waypoints(wp)


    self.conn.commit()

  # ---------------- Get Systems ----------------
  def get_systems(self):
    self.cursor.execute("SELECT symbol FROM systems")
    return [row[0] for row in self.cursor.fetchall()]

  # ---------------- Insert Method ----------------
  def insert_ship(self, ship):
    self.cursor.execute("""
      INSERT OR REPLACE INTO ships (
        symbol, name, faction, role
      ) VALUES (?, ?, ?, ?)
    """, (
      ship.symbol,
      ship.name,
      ship.faction,
      ship.role.value if ship.role else None
    ))
    self.conn.commit()

  # ---------------- Get Method ----------------
  def get_ship(self, symbol):
    self.cursor.execute("SELECT symbol FROM ships")
    return [row[0] for row in self.cursor.fetchall()]

# ===== Usage Example =====

  def close(self):
    self.conn.close()

if __name__ == "__main__":
  db = Database("kospacetraders.sqlite")
  db._create_table
  db.close()