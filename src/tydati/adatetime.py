from __future__ import annotations

from datetime import datetime, tzinfo
from typing import cast, TypeVar, Type


class realtzinfo(tzinfo):
    def __init__(self):
        ...


_C = TypeVar("_C")


class _ClassBranding:
    @classmethod
    def _brand(cls: Type[_C], o: object) -> _C:
        o.__class__ = cls
        return cast(cls, o)



class adatetime(datetime, _ClassBranding):
    def __init__(self):
        ...

    @classmethod
    def fromtimestamp(cls, t: float, /, tz: realtzinfo) -> adatetime:  # type:ignore[override]
        return cls._brand(super().fromtimestamp(t, tz))

class datetimeutc(adatetime):
    ...

class ndatetime(datetime):
    ...
