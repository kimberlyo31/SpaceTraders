import  { ContractDetailsPanelProps } from "../interfaces";
function renderContractDetails(
  key: string,
  value: any,
  path: string[] = [],
  level: number = 0
): React.ReactNode[] {
  const rows: React.ReactNode[] = [];
  const indent = level * 16;

  const currentPath = [...path, key];
  const pathString = currentPath.join("."); // unique key based on full path

  if (value && typeof value === "object" && !Array.isArray(value)) {
    // Parent row
    rows.push(
      <div
        key={pathString}
        className="grid grid-cols-2 border-b border-cyan-300/10 py-2"
        style={{ paddingLeft: indent }}
      >
        <div className="font-semibold text-cyan-300">{key}</div>
        <div></div>
      </div>
    );

    // Render subfields recursively
    Object.entries(value).forEach(([subKey, subVal]) => {
      rows.push(...renderContractDetails(subKey, subVal, currentPath, level + 1));
    });
  } else if (Array.isArray(value)) {
    rows.push(
      <div
        key={pathString}
        className="grid grid-cols-2 border-b border-cyan-300/10 py-2"
        style={{ paddingLeft: indent }}
      >
        <div className="font-semibold text-cyan-300">{key}</div>
        <div>{value.join(", ")}</div>
      </div>
    );
  } else {
    rows.push(
      <div
        key={pathString}
        className="grid grid-cols-2 border-b border-cyan-300/10 py-2"
        style={{ paddingLeft: indent }}
      >
        <div className="font-semibold text-cyan-300">{key}</div>
        <div>{String(value)}</div>
      </div>
    );
  }

  return rows;
}

export default function ContractDetailsPanel({ contract }: ContractDetailsPanelProps) {

  return (
    <div className="w-[420px] panel-glass border-l border-cyan-400/25 glow-cyan overflow-y-auto">
      <h2 className="text-xl font-bold p-5 border-b border-cyan-300/20 text-cyan-300 tracking-wider">
        {contract.type}
      </h2>
      <div className="p-6 space-y-6">

        <div className="grid grid-cols-1">
          {Object.entries(contract).flatMap(([key, value]) => renderContractDetails(key, value))}
        </div>
      </div>
    </div>
  );
}