export interface Ship {
  symbol: string;
  [key: string]: any;
}
export interface System {
  symbol: string;
  [key: string]: any;
}

export interface Waypoint {
  symbol: string;
  [key: string]: any;
}
export interface WaypointPanelProps {
  waypoints: Waypoint[];
  onSelectShip: (waypoint: Waypoint) => void;
}
export interface ShipDetailsPanelProps {
  ship: Ship;
  onDiscoverSystems: (newSystems: System[]) => void;
}

export interface FleetPanelProps {
  ships: Ship[];
  onSelectShip: (ship: Ship) => void;
  onScanWaypoints: (waypoints: Waypoint[]) => void;
}
export interface Contract {
  symbol: string;
  [key: string]: any;
}

export interface ContractPanelProps {
  contract: Contract;
  onSelectContract: (contract: Contract) => void;
}

export interface ContractDetailsPanelProps {
  contract: Contract;
}


export interface SystemPanelProps {
  system: System;
}