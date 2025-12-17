"use client"
import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import FleetPanel from "../components/FleetPanel";
import ContractsPanel from "../components/ContractsPanel";
import SystemPanel from "../components/SystemPanel";
import * as Interfaces from "../interfaces";
import ContractDetailsPanel from "@/components/ContractDetailsPanel";
import WaypointPanel from "@/components/WaypointPanel";

export default function Home() {
  const [contracts, setContracts] = useState<Interfaces.Contract[]>([]);
  const [selectedContract, setSelectedContract] = useState<Interfaces.Contract | null>(null);
  const [activeSection, setActiveSection] = useState<string>("fleet");
  const [ships, setShips] = useState<Interfaces.Ship[]>([]);
  const [systems, setSystems] = useState<Interfaces.System[]>([]);
  const [waypoints, setWaypoints] = useState<Interfaces.Waypoint[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/ships")
      .then((res) => res.json())
      .then((data: Interfaces.Ship[]) => setShips(data));

    fetch("http://localhost:8000/api/contracts")
      .then((res) => res.json())
      .then((data: Interfaces.Contract[]) => setContracts(data));
  }, []);
  const handleScanWaypoints = (scanned: Interfaces.Waypoint[]) => {
    setWaypoints(prev => {
      const existing = new Set(prev.map(w => w.symbol));
      const newOnes = scanned.filter(w => !existing.has(w.symbol));
      return [...prev, ...newOnes];
    });
  };
  return (
    <div className="flex h-screen bg-gradient-to-br from-black via-gray-900 to-black text-gray-100">
      <Sidebar active={activeSection} onSelect={setActiveSection} />

      {activeSection === "fleet" && (
        <FleetPanel 
          ships={ships}
          onScanWaypoints={handleScanWaypoints} />
      )}

      {activeSection === "contracts" && (
          <ContractsPanel contracts={contracts}/>
      )}

      {activeSection === "systems" && (
        <SystemPanel systems={systems} />
      )}

      {activeSection === "waypoints" && (
        <WaypointPanel waypoints={waypoints} />
      )}
    </div>
  );
}
