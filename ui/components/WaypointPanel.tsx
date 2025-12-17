import { useEffect, useState } from "react";
import { Waypoint,WaypointPanelProps } from "../interfaces";
import WaypointCard from "./WaypointCard";
import WaypointModal from "./WaypointModal";

export default function WaypointPanel({ waypoints}: WaypointPanelProps) {
  const [selectedWaypoint, setSelectedWaypoint] = useState<Waypoint | null>(null);
  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Waypoints</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {waypoints.map((waypoint) => (
          <WaypointCard
            key={waypoint.symbol}
            waypoint={waypoint}
            onClick={() => setSelectedWaypoint(waypoint)}
          />
        ))}
      </div>
      {selectedWaypoint && (
        <WaypointModal
          waypoint={selectedWaypoint}
          onClose={() => setSelectedWaypoint(null)}
        />
      )}
    </div>
  );
}