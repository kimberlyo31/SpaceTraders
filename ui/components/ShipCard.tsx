import { Ship } from "../interfaces";

interface Props {
  ship: Ship;
  onClick: () => void;
}

export default function ShipCard({ ship, onClick }: Props) {
  const fuel = ship.fuel ?? { current: 0, capacity: 1 };

  const fuelPct = Math.round((fuel.current / fuel.capacity) * 100);

  return (
    <div
      onClick={onClick}
      className="cursor-pointer bg-gray-800 rounded-xl p-4 shadow hover:bg-gray-700 transition"
    >
      <h2 className="font-semibold text-lg">{ship.symbol}</h2>

      <p className="text-sm opacity-75">
        {ship.registration?.role ?? "Unknown Role"}
      </p>

      <div className="mt-3">
        <p className="text-sm">
          Fuel: {fuel.current} / {fuel.capacity}
        </p>

        <div className="w-full bg-gray-600 h-2 rounded mt-1">
          <div
            className="bg-green-500 h-full rounded"
            style={{ width: `${fuelPct}%` }}
          />
        </div>
      </div>
    </div>
  );
}
