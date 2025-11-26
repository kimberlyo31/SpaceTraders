"use client";

import { useEffect, useState } from "react";
import ShipList from "../components/ShipList";
import ContractList from "../components/ContractList";
import ActionButton from "../components/ActionButton";

export default function Home() {
  const [ships, setShips] = useState([]);
  const [contracts, setContracts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/ships")
      .then(res => res.json())
      .then(setShips);

    // fetch("http://localhost:8000/api/contracts")
    //   .then(res => res.json())
    //   .then(setContracts);
  }, []);

  const handleRefresh = () => {
    fetch("http://localhost:8000/api/refresh")
      .then(res => res.json())
      .then(data => {
        setShips(data.ships);
        setContracts(data.contracts);
      });
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">SpaceTraders Dashboard</h1>
      <ActionButton text="Refresh Data" onClick={handleRefresh} />

      <div className="mt-6">
        <h2 className="text-2xl font-semibold mb-2">Fleet</h2>
        <ShipList ships={ships} />
      </div>

      {/* <div className="mt-6">
        <h2 className="text-2xl font-semibold mb-2">Contracts</h2>
        <ContractList contracts={contracts} />
      </div> */}
    </div>
  );
}
