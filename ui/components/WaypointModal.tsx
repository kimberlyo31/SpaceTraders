import { Waypoint,Ship } from "../interfaces";

import { useEffect, useState } from "react";
interface Props {
  waypoint: Waypoint;
  onClose: () => void;
}

export default function WaypointModal({ waypoint, onClose }: Props) {
  const [shipyardShips, setShipyardShips] = useState<string[] | null>(null);
  const hasShipyard = waypoint.traits?.some(
    t => t.symbol === "SHIPYARD"
  );
  const getShipyardShips = async() => {
    try {
      const res = await fetch('http://localhost:8000/api/getShipyardShips' , {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ waypointSymbol: waypoint.symbol, systemSymbol: waypoint.systemSymbol }),
      });

      const data = await res.json();

      const types = data.availableShips.map(
        (s: { type: string }) => s.type
      );

      setShipyardShips(types);
    } catch (err) {
      console.error(err);
    }
  };
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-60">
      <div className="bg-gray-900 p-6 rounded-xl max-w-lg w-full">
        <button className="float-right" onClick={onClose}>✕</button>
        <h2 className="text-xl font-bold mb-4">{waypoint.symbol}</h2>

        <div className="space-y-2 text-sm">
          <p><strong>Type:</strong> {waypoint.type}</p>
          <p><strong>Traits:</strong> {waypoint.traits.map(t => t.symbol).join(', ')}</p>
          <p><strong>Orbitals:</strong> {waypoint.orbitals.map(o => o.symbol).join(', ')}</p>
          <p><strong>X,Y:</strong> {waypoint.x},{waypoint.y}</p>

        </div>
        {hasShipyard && (
          <button
            onClick={getShipyardShips}
            disabled={!!shipyardShips}
            className="mt-5 w-full bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50"
          >
            View Available Ships
          </button>
        )}
        {shipyardShips && (
          <p className="mt-3 text-sm">
            <strong>Available Ships:</strong> {shipyardShips.join(", ")}
          </p>
        )}
      </div>
    </div>
  );
}