import { Contract } from "../interfaces";

interface Props{
  contract: Contract
  onClick: () => void
}

export default function ContractCard({contract, onClick}:Props) {
  const contractType = contract.type;

  return (
    <div
      onClick={onClick}
      className="cursor-pointer bg-gray-800 rounded-xl p-4 shadow hover:bg-gray-700 transition"
    >
      <h2 className="font-semibold text-lg">{contract.type}</h2>
      <p className="text-sm opacity-75">
        {contract.terms?.deadline ?? "Unknown Role"}
      </p>

      <div className="mt-3">
        <p className="text-sm">
          Payment: {contract.terms.payment.onAccepted} / {contract.terms.payment.onFulfilled}
        </p>
      </div>
    </div>
  )
}