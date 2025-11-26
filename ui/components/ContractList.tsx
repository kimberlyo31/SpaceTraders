export default function ContractList({ contracts }: { contracts: any[] }) {
  if (!contracts || contracts.length === 0) return <p>No contracts found.</p>;

  return (
    <ul className="space-y-2">
      {contracts.map(contract => (
        <li key={contract.id} className="p-3 bg-gray-100 rounded shadow">
          <strong>{contract.type}</strong> — {contract.status}
        </li>
      ))}
    </ul>
  );
}
