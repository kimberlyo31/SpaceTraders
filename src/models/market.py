from dataclasses import dataclass
from src.enums import TradeGoodSymbol, TransactionType, TradeType, Supply, Activity

@dataclass
class TradeGood:
  symbol: TradeGoodSymbol
  name: str
  description: str
  units: int
  
  @staticmethod
  def from_json(payload):
    return TradeGood(
      symbol=TradeGoodSymbol(payload["symbol"]),
      name=payload["name"],
      description=payload["description"],
      units=payload["units"]
    )

@dataclass
class MarketTradeGood:
  symbol: TradeGoodSymbol
  trade_type: TradeType
  trade_volume: int
  supply: Supply
  purchase_price: int
  sell_price: int
  activity: Activity | None = None
    
  @staticmethod
  def from_json(payload):
    return MarketTradeGood(
      symbol=TradeGoodSymbol(payload['symbol']),
      trade_type= TradeType(payload['type']),
      trade_volume=payload['tradeVolume'],
      supply=Supply(payload['supply']),
      purchase_price=payload['purchasePrice'],
      sell_price=payload['sellPrice'],
      activity=Activity(payload['activity']) if payload.get('activity') else None
    ) 
  
@dataclass
class ImportExport:
  symbol: TradeGoodSymbol
  name: str
  description: str
  
  @staticmethod
  def from_json(payload):
    return ImportExport(
      symbol=TradeGoodSymbol(payload['symbol']),
      name=payload['name'],
      description=payload['description']
    )
        
@dataclass
class Transaction:
  waypoint_symbol: str
  ship_symbol: str
  trade_symbol: TradeGoodSymbol
  transaction_type: TransactionType
  units: int
  price_per_unit: int
  total_price: int
  timestamp: str
  
  @staticmethod
  def from_json(payload):
    return Transaction(
      waypoint_symbol=payload['waypointSymbol'],
      ship_symbol=payload['shipSymbol'],
      trade_symbol=TradeGoodSymbol(payload['tradeSymbol']),
      transaction_type=TransactionType(payload['type']),
      units=payload['units'],
      price_per_unit=payload['pricePerUnit'],
      total_price=payload['totalPrice'],
      timestamp=payload['timestamp']
    )

@dataclass
class Market:
  symbol: str
  exports: list[ImportExport]
  imports: list[ImportExport]
  exchange: list[ImportExport]
  transaction: list[Transaction] | None = None
  tradegood: list[MarketTradeGood] | None = None
  
  @staticmethod
  def from_json(payload):
    return Market(
      symbol=payload["symbol"],
      exports=[ImportExport.from_json(item) for item in payload.get("exports", [])],
      imports=[ImportExport.from_json(item) for item in payload.get("imports", [])],
      exchange=[ImportExport.from_json(item) for item in payload.get("exchange", [])],
      transaction=[Transaction.from_json(t) for t in payload.get("transactions", [])] 
        if payload.get("transactions") else None,
      tradegood=[MarketTradeGood.from_json(tg) for tg in payload.get("tradeGoods", [])]
        if payload.get("tradeGoods") else None
    )
  
  