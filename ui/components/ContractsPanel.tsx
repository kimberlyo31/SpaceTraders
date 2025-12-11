import { useEffect, useState } from "react";
import { Contract,ContractPanelProps } from "../interfaces";
import ContractCard from "./ContractCard";
import ContractModal from "./ContractModal";

export default function ContractPanel({ contracts}: ContractPanelProps) {
  const [selectedContract, setSelectedContract] = useState<Contract | null>(null);
  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Fleet</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {contracts.map((contract) => (
          <ContractCard
            key={contract.id}
            contract={contract}
            onClick={() => setSelectedContract(contract)}
          />
        ))}
      </div>
      {selectedContract && (
        <ContractModal
          contract={selectedContract}
          onClose={() => setSelectedContract(null)}
        />
      )}
    </div>
  );
}