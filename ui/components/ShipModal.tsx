import { Ship,Waypoint } from "../interfaces";
import { useEffect, useState } from "react";
interface Props {
  ship: Ship;
  onClose: () => void;
  onScan: (waypoints: Waypoint[]) => void;
}

export default function ShipModal({ ship, onClose, onScan }: Props) {
  const takeAction = async (action: "dock" | "orbit" | "scan") => {
    try {
      const res = await fetch(`http://localhost:8000/api/${action}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symbol: ship.symbol }),
      });

      const data = await res.json();
      console.log(`${action} result:`, data);

      if (action === "scan" && data.waypoints) {
        onScan(data.waypoints);
      }
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-60">
      <div className="bg-gray-900 p-6 rounded-xl max-w-lg w-full">
        <button className="float-right" onClick={onClose}>✕</button>
        <h2 className="text-xl font-bold mb-4">{ship.symbol}</h2>

        <div className="space-y-2 text-sm">
          <p><strong>Role:</strong> {ship.registration?.role}</p>
          <p><strong>Status:</strong> {ship.nav?.status}</p>
          <p><strong>Location:</strong> {ship.nav?.waypointSymbol}</p>
          <p>
            <strong>Fuel:</strong> {ship.fuel?.current}/{ship.fuel?.capacity}
          </p>
        </div>

        <div className="mt-6 flex gap-3">
          <button
            className="bg-blue-600 px-4 py-2 rounded"
            onClick={() => takeAction("dock")}
          >
            Dock
          </button>

          <button
            className="bg-purple-600 px-4 py-2 rounded"
            onClick={() => takeAction("orbit")}
          >
            Orbit
          </button>

          <button
            className="bg-green-600 px-4 py-2 rounded"
            onClick={() => takeAction("scan")}
          >
            Scan
          </button>
        </div>
      </div>
    </div>
  );
}
