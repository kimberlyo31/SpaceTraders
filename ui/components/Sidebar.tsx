interface SidebarProps {
  active: string;
  onSelect: (section: string) => void;
}

export default function Sidebar({ active, onSelect }: SidebarProps) {
  const items = ["fleet", "agent", "contracts", "systems"];

  return (
    <div className="w-52 panel-glass border-r border-cyan-400/30 glow-cyan p-4 flex flex-col">
      <h1 className="text-2xl font-bold tracking-wide text-cyan-300 mb-6">
        Space Traders
      </h1>
      {items.map((item) => (
        <button
          key={item}
          onClick={() => onSelect(item)}
          className={`w-full text-left py-2 px-3 rounded-lg 
            hover:bg-[#162033] hover:text-cyan-300 transition-all tracking-wide
            ${active === item ? "bg-[#162033] text-cyan-300 glow-cyan font-semibold" : ""
          }`}
        >
          {item.toUpperCase()}
        </button>
      ))}
    </div>
  );
}
