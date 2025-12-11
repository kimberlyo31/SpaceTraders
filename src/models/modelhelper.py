from enum import Enum
from dataclasses import dataclass, asdict, is_dataclass

def serialize(obj):
  if is_dataclass(obj):
    return {k: serialize(v) for k, v in asdict(obj).items()}
  if isinstance(obj, Enum):
    return obj.value
  if isinstance(obj, list):
    return [serialize(i) for i in obj]
  if isinstance(obj, dict):
    return {k: serialize(v) for k, v in obj.items()}
  return obj