from __future__ import annotations

import datetime as dt
from typing import Optional

from dateutil.parser import parse


def convert_to_datetime(datetime_str: Optional[str]) -> Optional[dt.datetime]:
    """Callback to convert string to datetime given as an iso8601 timestamp."""
    if datetime_str is None:
        return None

    try:
        return parse(datetime_str)
    except Exception:
        raise ValueError(f"'{datetime_str}' is not a valid iso8601 timestamp")
