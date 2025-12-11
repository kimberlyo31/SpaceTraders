"use client";

import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import FleetPanel from "../components/FleetPanel";
import ContractPanel from "../components/ContractsPanel";
import SystemPanel from "../components/SystemPanel";
import * as Interfaces from "../interfaces";
import ContractDetailsPanel from "@/components/ContractDetailsPanel";

export default function Home() {
  const [contracts, setContracts] = useState<Interfaces.Contract[]>([]);
  const [selectedContract, setSelectedContract] = useState<Interfaces.Contract | null>(null);
  const [activeSection, setActiveSection] = useState<string>("fleet");
  const [ships, setShips] = useState<Interfaces.Ship[]>([]);
  const [systems, setSystems] = useState<Interfaces.System[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/ships")
      .then((res) => res.json())
      .then((data: Interfaces.Ship[]) => setShips(data));

    fetch("http://localhost:8000/api/contracts")
      .then((res) => res.json())
      .then((data: Interfaces.Contract[]) => setContracts(data));
  }, []);

  return (
    <div className="flex h-screen bg-gradient-to-br from-black via-gray-900 to-black text-gray-100">
      <Sidebar active={activeSection} onSelect={setActiveSection} />

      {activeSection === "fleet" && (
        <FleetPanel ships={ships} />
      )}

      {activeSection === "contracts" && (
        <>
          <ContractPanel
            contracts={contracts}
            onSelectContract={setSelectedContract}
          />
          {selectedContract && (
            <ContractDetailsPanel contract={selectedContract} />
          )}
        </>
      )}

      {activeSection === "systems" && (
        <SystemPanel systems={systems} />
      )}
    </div>
  );
}
