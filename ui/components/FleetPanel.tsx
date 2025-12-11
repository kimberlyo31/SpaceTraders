import { useEffect, useState } from "react";
import ShipCard from "./ShipCard";
import ShipModal from "./ShipModal";
import { Ship, FleetPanelProps } from "../interfaces";

export default function FleetPanel({ ships }: FleetPanelProps) {
  const [selectedShip, setSelectedShip] = useState<Ship | null>(null);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Fleet</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {ships.map((ship) => (
          <ShipCard
            key={ship.symbol}
            ship={ship}
            onClick={() => setSelectedShip(ship)}
          />
        ))}
      </div>

      {selectedShip && (
        <ShipModal
          ship={selectedShip}
          onClose={() => setSelectedShip(null)}
        />
      )}
    </div>
  );
}
