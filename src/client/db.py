import sqlite3
import json
from typing import List, Tuple, Optional
from src.models.ship import *
from src.models.system import *
from src.models.market import *
from src.enums import *


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
        role TEXT,
        nav TEXT,
        crew TEXT,
        frame TEXT,
        reactor TEXT,
        engine TEXT,
        cargo TEXT,
        fuel TEXT,
        cooldown TEXT,
        modules TEXT,
        mounts TEXT
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
        is_under_construction INTEGER NOT NULL,
        orbits TEXT,
        faction_name TEXT,
        faction_symbol TEXT,
        chart_submitted_by TEXT,
        chart_submitted_on TEXT,
        traits TEXT,
        modifiers TEXT,
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
    traits_json = json.dumps([{
        "symbol": t.symbol,
        "name": t.name,
        "description": t.description
      } for t in waypoint.traits]) if waypoint.traits else None

    modifiers_json = json.dumps([{
        "symbol": m.symbol,
        "name": m.name,
        "description": m.description
      } for m in waypoint.modifiers]) if waypoint.modifiers else None

    self.cursor.execute("""
        INSERT OR REPLACE INTO waypoints (
          symbol, system_symbol, type, x, y, is_under_construction,
          orbits, faction_name, faction_symbol,
          chart_submitted_by, chart_submitted_on,
          traits, modifiers
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      """, (
        waypoint.symbol, waypoint.system_symbol, waypoint.waypoint_type, waypoint.x, waypoint.y,
        int(waypoint.isUnderConstruction),
        waypoint.orbits,
        waypoint.faction.name if waypoint.faction else None,
        waypoint.faction.symbol if waypoint.faction else None,
        waypoint.chart.submitted_by.name if waypoint.chart and waypoint.chart.submitted_by else None,
        waypoint.chart.submitted_on if waypoint.chart else None,
        traits_json,
        modifiers_json
      ))

  # ---------------- Get Waypoints ----------------
  def get_waypoints(self):
    self.cursor.execute("SELECT * FROM waypoints")
    waypoints = []
    for row in self.cursor.fetchall():
      (
        symbol, system_symbol, type_, x, y, is_under_construction,
        orbits, faction_name, faction_symbol, chart_submitted_by, chart_submitted_on,
        traits_json, modifiers_json
      ) = row

      traits = [WaypointTrait.from_json(t) for t in json.loads(traits_json)] if traits_json else []
      modifiers = [WaypointModifier.from_json(m) for m in json.loads(modifiers_json)] if modifiers_json else []

      chart = None
      if chart_submitted_by and chart_submitted_on:
        chart = Chart(
          waypoint_symbol=symbol,
          submitted_by=Agent({"name": chart_submitted_by}),
          submitted_on=chart_submitted_on
        )

      faction = None
      if faction_name and faction_symbol:
        faction = Faction(name=faction_name, symbol=faction_symbol)

      waypoint = Waypoint(
        symbol=symbol,
        waypoint_type=WaypointType(type_),
        system_symbol=system_symbol,
        x=x,
        y=y,
        orbitals=[],  # optional: populate if you store orbitals separately
        traits=traits,
        isUnderConstruction=bool(is_under_construction),
        orbits=orbits,
        faction=faction,
        modifiers=modifiers,
        chart=chart
      )
      waypoints.append(waypoint)
    return waypoints
      
  def insert_system(self, system: System):
    self.cursor.execute("""
      INSERT OR REPLACE INTO systems (symbol, sector_symbol, type, x, y, constellation, name)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (system.symbol, system.sector_symbol, system.type, system.x, system.y, system.constellation, system.name))

    for faction in system.factions:
      self.cursor.execute("""
        INSERT INTO factions (system_symbol, name, symbol) VALUES (?, ?, ?)
      """, (system.symbol, faction.name, faction.symbol))

    for wp in system.waypoints:
      self.insert_waypoints(wp)

      for o in wp.orbitals:
        self.cursor.execute("""
          INSERT INTO waypoint_orbitals (waypoint_symbol, symbol) VALUES (?, ?)
        """, (wp.symbol, o.symbol))

    self.conn.commit()

  # ---------------- Get Systems ----------------
  def get_systems(self):
    self.cursor.execute("SELECT * FROM systems")
    systems = []
    for row in self.cursor.fetchall():
      symbol, sector_symbol, type_, x, y, constellation, name, waypoints_json, factions_json = row

      waypoints_data = json.loads(waypoints_json) if waypoints_json else []
      waypoints = [Waypoint.from_json(wp) for wp in waypoints_data]

      factions_data = json.loads(factions_json) if factions_json else []
      factions = [Faction.from_json(f) for f in factions_data]

      system = System(
        symbol=symbol,
        sector_symbol=sector_symbol,
        type=SystemType(type_),
        x=x,
        y=y,
        waypoints=waypoints,
        factions=factions,
        contsellation=constellation,
        name=name
      )
      systems.append(system)
    return systems

  # ---------------- Insert Method ----------------
  def insert_ship(self, ship):
    self.cursor.execute("""
      INSERT OR REPLACE INTO ships (
        symbol, name, faction, role, nav, crew, frame, reactor,
        engine, cargo, fuel, cooldown, modules, mounts
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
      ship.symbol,
      ship.name,
      ship.faction,
      ship.role.value if ship.role else None,
      json.dumps(serialize(ship.nav)) if ship.nav else None,
      json.dumps(serialize(ship.crew)) if ship.crew else None,
      json.dumps(serialize(ship.frame)) if ship.frame else None,
      json.dumps(serialize(ship.reactor)) if ship.reactor else None,
      json.dumps(serialize(ship.engine)) if ship.engine else None,
      json.dumps(serialize(ship.cargo)) if ship.cargo else None,
      json.dumps(serialize(ship.fuel)) if ship.fuel else None,
      json.dumps(serialize(ship.cooldown)) if ship.cooldown else None,
      json.dumps([serialize(m) for m in ship.modules]) if ship.modules else None,
      json.dumps([serialize(mt) for mt in ship.mounts]) if ship.mounts else None
    ))
    self.conn.commit()

  # ---------------- Get Method ----------------
  def get_ship(self, symbol):
    self.cursor.execute("SELECT * FROM ships WHERE symbol = ?", (symbol,))
    row = self.cursor.fetchone()
    if not row:
      return None

    (
      symbol, name, faction, role, nav_json, crew_json, frame_json,
      reactor_json, engine_json, cargo_json, fuel_json, cooldown_json,
      modules_json, mounts_json
    ) = row

    # Deserialize nested objects
    nav = Nav.from_json(json.loads(nav_json)) if nav_json else None
    crew = Crew.from_json(json.loads(crew_json)) if crew_json else None
    frame = Frame.from_json(json.loads(frame_json)) if frame_json else None
    reactor = Reactor.from_json(json.loads(reactor_json)) if reactor_json else None
    engine = Engine.from_json(json.loads(engine_json)) if engine_json else None

    cargo_data = json.loads(cargo_json) if cargo_json else None
    cargo = Cargo(
      capacity=cargo_data['capacity'],
      units=cargo_data['units'],
      inventory=[TradeGood.from_json(i) for i in cargo_data['inventory']]
    ) if cargo_data else None

    fuel = Fuel.from_json(json.loads(fuel_json)) if fuel_json else None
    cooldown = Cooldown.from_json(json.loads(cooldown_json)) if cooldown_json else None

    modules = [Module.from_json(m) for m in json.loads(modules_json)] if modules_json else []
    mounts = [Mount.from_json(m) for m in json.loads(mounts_json)] if mounts_json else []

    return Ship(
      symbol=symbol,
      name=name,
      faction=faction,
      role=ShipRole(role),
      nav=nav,
      crew=crew,
      frame=frame,
      reactor=reactor,
      engine=engine,
      cargo=cargo,
      fuel=fuel,
      cooldown=cooldown,
      modules=modules,
      mounts=mounts
    )
# ===== Usage Example =====

  def close(self):
    self.conn.close()

if __name__ == "__main__":
  db = Database("kospacetraders.sqlite")
  db._create_table
  db.close()