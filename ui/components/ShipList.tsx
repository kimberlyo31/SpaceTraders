export default function ShipList({ ships }: { ships: any[] }) {
  if (!ships || ships.length === 0) return <p>No ships found.</p>;

  return (
    <ul className="space-y-2">
      {ships.map(ship => (
        <li key={ship.symbol} className="p-3 bg-gray-100 text-gray-900 rounded shadow">
          <strong>{ship.symbol}</strong> — {ship.nav?.status || "Unknown"}
        </li>
      ))}
    </ul>
  );
}
