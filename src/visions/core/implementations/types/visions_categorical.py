import pandas.api.types as pdt
import pandas as pd

from visions.core.model.model_relation import relation_conf
from visions.core.model.type import VisionsBaseType


class visions_categorical(VisionsBaseType):
    """**Categorical** implementation of :class:`visions.core.model.type.VisionsBaseType`.

    Examples:
        >>> x = pd.Series([True, False, 1], dtype='category')
        >>> x in visions_categorical
        True
    """

    @classmethod
    def get_relations(cls) -> dict:
        from visions.core.implementations.types import visions_generic

        return {visions_generic: relation_conf(inferential=False)}

    @classmethod
    def contains_op(cls, series: pd.Series) -> bool:
        return pdt.is_categorical_dtype(series)