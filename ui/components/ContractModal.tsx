import { Contract } from  "../interfaces"

interface Props {
  contract: Contract
  onClose: () => void
}

export default function ContractModal({contract, onClose}: Props) {
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-60">
      <div className="bg-gray-900 p-6 rounded-xl max-w-lg w-full">
        <button className="float-right" onClick={onClose}>✕</button>
        <h2 className="text-xl font-bold mb-4">{contract.type}</h2>

        <div className="space-y-4 text-sm">
          {contract.terms?.deliver?.map((deliver, index) => (
            <div
              key={index}
              className="border border-gray-700 rounded-lg p-3 bg-gray-800"
            >
              <p>
                <strong>Trade Symbol:</strong> {deliver.tradeSymbol}
              </p>

              <p>
                <strong>Destination:</strong> {deliver.destinationSymbol}
              </p>

              <p>
                <strong>Progress:</strong> {deliver.unitsFulfilled}/{deliver.unitsRequired}
              </p>
            </div>
          ))}

          <p className="pt-4">
            <strong>Payment:</strong> {contract.terms.payment.onAccepted} / {contract.terms.payment.onFulfilled}
          </p>
        </div>
      </div>
    </div>
  );
}