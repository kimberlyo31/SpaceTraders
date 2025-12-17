from enum import Enum
from dataclasses import dataclass, asdict, is_dataclass, fields
import json

def mserialize(obj):
  if is_dataclass(obj):
    return {k: mserialize(v) for k, v in asdict(obj).items()}
  if isinstance(obj, Enum):
    return obj.value
  if isinstance(obj, list):
    return [mserialize(i) for i in obj]
  if isinstance(obj, dict):
    return {k: mserialize(v) for k, v in obj.items()}
  return obj

def mdeserialize(data, cls):
    """
    Deserialize `data` (dict or JSON string) into instance of class `cls`.
    This matches your serialize() behavior.
    """
    
    # If JSON string → convert to dict
    if isinstance(data, str):
        data = json.loads(data)

    # If the target class has its own from_json, use it
    if hasattr(cls, "from_json") and callable(getattr(cls, "from_json")):
        return cls.from_json(data)

    # If it's a dataclass, reconstruct it
    if is_dataclass(cls):
        kwargs = {}
        for f in fields(cls):
            value = data.get(f.name)

            if value is None:
                kwargs[f.name] = None
                continue

            # If field type is a list
            if getattr(f.type, "__origin__", None) is list:
                inner_type = f.type.__args__[0]
                kwargs[f.name] = [
                    mdeserialize(item, inner_type) for item in value
                ]
                continue

            # If field type is an Enum
            if isinstance(f.type, type) and issubclass(f.type, Enum):
                kwargs[f.name] = f.type(value)
                continue

            # Nested dataclass or object
            if is_dataclass(f.type):
                kwargs[f.name] = mdeserialize(value, f.type)
                continue

            # Primitive type
            kwargs[f.name] = value

        return cls(**kwargs)

    # If dict → return as-is
    if isinstance(data, dict):
        return {k: mdeserialize(v, type(v)) for k, v in data.items()}

    # Primitive value
    return data
