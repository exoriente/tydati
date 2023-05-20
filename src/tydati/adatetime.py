from __future__ import annotations

from datetime import datetime, tzinfo


class realtzinfo(tzinfo):
    def __init__(self):
        ...


class adatetime(datetime):
    def __init__(self):
        ...

    @classmethod
    def fromtimestamp(cls, t: float, /, tz: realtzinfo) -> adatetime:  # type:ignore[override]
        return super().fromtimestamp(t, tz)


class datetimeutc(adatetime):
    ...

class ndatetime(datetime):
    ...
