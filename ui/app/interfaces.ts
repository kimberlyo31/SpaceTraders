export interface Ship {
  symbol: string;
  [key: string]: any;
}
export interface System {
  symbol: string;
  [key: string]: any;
}

export interface ShipDetailsPanelProps {
  ship: Ship;
  onDiscoverSystems: (newSystems: System[]) => void;
}

export interface FleetPanelProps {
  ships: Ship[];
  onSelectShip: (ship: Ship) => void;
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