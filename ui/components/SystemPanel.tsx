import { System,SystemPanelProps } from "../interfaces";

export default function SystemPanel({ systems }: SystemPanelProps) {
  return (
    <div className="w-[400px] panel-glass border-l border-pink-400/25 glow-magenta overflow-y-auto">
      <h2 className="text-xl font-bold mb-4 text-pink-300 p-4 border-b border-pink-300/20">
        SYSTEMS
      </h2>
      <div className="flex flex-col divide-y divide-pink-300/10">
        {systems.map((system: System, index: number) => (
          <button
            key={`${system.symbol}-${index}`} // now index exists
            className="p-4 hover:bg-pink-400/10 hover:text-pink-200 transition text-left text-lg"
          >
            {system.symbol}
          </button>
        ))}
      </div>
    </div>
  );
}