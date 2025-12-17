from dataclasses import dataclass
from src.enums import TradeGoodSymbol,ContractType
from .modelhelper import mserialize
@dataclass
class Payment:
  on_accepted: int
  on_fulfilled: int
  
  @staticmethod
  def from_json(payload):
    return Payment(
      on_accepted=payload['onAccepted'],
      on_fulfilled=payload['onFulfilled']
    )
  def to_json(self):
    return mserialize(self)    
@dataclass
class Deliver:
  trade_symbol: TradeGoodSymbol
  destination_symbol: str
  units_required: int
  units_fulfilled: int
  
  @staticmethod
  def from_json(payload):
    return Deliver(
      trade_symbol=payload['tradeSymbol'],
      destination_symbol=payload['destinationSymbol'],
      units_required=payload['unitsRequired'],
      units_fulfilled=payload['unitsFulfilled']
    )
  def to_json(self):
    return mserialize(self)
@dataclass
class Terms:
  deadline: str
  payment: Payment
  deliver: Deliver | None = None
  
  @staticmethod
  def from_json(payload):
    return Terms(
      deadline=payload['deadline'],
      payment=Payment(payload['payment']),
      deliver=Deliver(payload.get('deliver'))
    )
  def to_json(self):
    return mserialize(self)    
@dataclass
class Contract:
  id: str
  faction_symbol: str
  contract_type: ContractType
  terms: Terms
  accepted: bool
  fulfilled: bool
  deadline_to_accept: str | None = None
  
  @staticmethod
  def from_json(payload):
    return Contract(
      id=payload['id'],
      faction_symbol=payload['factionSymbol'],
      contract_type=ContractType(payload['type']),
      terms=Terms(payload['terms']),
      accepted=payload['accepted'],
      fulfilled=payload['fulfilled'],
      deadline_to_accept=payload.get('deadlineToAccept')
    )
  def to_json(self):
    return mserialize(self)