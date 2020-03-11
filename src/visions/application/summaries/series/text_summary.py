from collections import Counter
from typing import Dict

import pandas as pd

from tangled_up_in_unicode import category, category_long, script, block, block_abbr


def get_character_counts(series) -> Dict[str, int]:
    """Function to return the character counts

    Args:
        series: the Series to process

    Returns:
        A dict with character counts
    """
    return dict(Counter(series.str.cat()))


def text_summary(series: pd.Series) -> dict:
    """

    Args:
        series: series to summarize

    Returns:

    """
    # Distribution of length
    summary = {"length": series.map(lambda x: len(str(x))).value_counts().to_dict()}

    # Unicode Character Summaries (category and script name)
    character_counts = get_character_counts(series)

    summary["category_short_values"] = {
        key: category(key) for key in character_counts.keys()
    }
    summary["category_alias_values"] = {
        key: category_long(value)
        for key, value in summary["category_short_values"].items()
    }
    summary["script_values"] = {key: script(key) for key in character_counts.keys()}
    summary["block_values"] = {key: block(key) for key in character_counts.keys()}
    summary["block_alias_values"] = {
        key: block_abbr(value) for key, value in summary["block_values"].items()
    }

    return summary
