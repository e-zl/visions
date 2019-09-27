import pandas as pd
from ipaddress import _BaseAddress, ip_address

from tenzing.core.model.models import tenzing_model


class tenzing_ip(tenzing_model):
    """**IP Address** (v4 and v6) implementation of :class:`tenzing.core.models.tenzing_model`.
    >>> from ipaddress import IPv4Address
    >>> x = pd.Series([IPv4Address('127.0.0.1'), IPv4Address('128.0.1.2')])
    >>> x in tenzing_ip
    True
    """

    @classmethod
    def contains_op(cls, series: pd.Series) -> bool:
        return series.apply(lambda x: isinstance(x, _BaseAddress)).all()

    @classmethod
    def cast_op(cls, series: pd.Series, operation=None) -> pd.Series:
        return series.apply(ip_address)
