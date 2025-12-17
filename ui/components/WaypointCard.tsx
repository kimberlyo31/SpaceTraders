import { Waypoint } from "../interfaces";

interface Props {
  waypoint: Waypoint;
  onClick: () => void;
}

export default function WaypointCard({ waypoint, onClick }: Props) {

  return (
    <div
      onClick={onClick}
      className="cursor-pointer bg-gray-800 rounded-xl p-4 shadow hover:bg-gray-700 transition"
    >
      <h2 className="font-semibold text-lg">{waypoint.symbol}</h2>

      <p className="text-sm opacity-75">
        {waypoint.type ?? "Unknown Type"}
      </p>

      <div className="mt-3">
        <p className="text-sm">
          Traits: {waypoint.traits.map(t => t.symbol).join(', ')}
        </p>

      </div>
    </div>
  );
}
