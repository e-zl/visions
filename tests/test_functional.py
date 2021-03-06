import pandas as pd
import numpy as np

from visions.functional import (
    infer_frame_type,
    infer_series_type,
    cast_frame,
    cast_series,
    detect_frame_type,
    detect_series_type,
)
from visions.types import String, Integer, DateTime, Complex
from visions.typesets import CompleteSet, StandardSet


def test_type_inference_frame():
    # Create a DataFrame with various string columns
    df = pd.DataFrame(
        {
            "latin": ["orange", "apple", "pear"],
            "cyrillic": ["Кириллица", "гласность", "демократија"],
            "mixed": ["Кириллица", "soep", "демократија"],
            "burmese": ["ရေကြီးခြင်း", "စက်သင်ယူမှု", "ဉာဏ်ရည်တု"],
            "digits": ["01234", "121223", "12312"],
            "specials": ["$", "%^&*(", "!!!~``"],
            "whitespace": ["\t", "\n", " "],
            "jiddisch": ["רעכט צו לינקס", "שאָסיי 61", "פּיצאַ איז אָנגענעם"],
            "arabic": ["بوب ديلان", "باتي فالنتين", "السيد الدف الرجل"],
            "playing_cards": ["🂶", "🃁", "🂻"],
        }
    )

    # Initialize the typeset
    typeset = CompleteSet()

    # Infer the column type
    types = infer_frame_type(df, typeset)
    assert types == {
        "latin": String,
        "cyrillic": String,
        "mixed": String,
        "burmese": String,
        "digits": Integer,
        "specials": String,
        "whitespace": String,
        "jiddisch": String,
        "arabic": String,
        "playing_cards": String,
    }


def test_type_inference_series():
    string_series = pd.Series(["(12.0+10.0j)", "(-4.0+6.2j)", "(8.0+2.0j)"])

    typeset = StandardSet()
    detected_type = infer_series_type(string_series, typeset)
    assert detected_type == Complex


def test_type_cast_frame():
    df = pd.DataFrame(
        {
            "latin": ["orange", "apple", "pear"],
            "cyrillic": ["Кириллица", "гласность", "демократија"],
            "mixed": ["Кириллица", "soep", "демократија"],
            "burmese": ["ရေကြီးခြင်း", "စက်သင်ယူမှု", "ဉာဏ်ရည်တု"],
            "digits": ["01234", "121223", "12312"],
            "specials": ["$", "%^&*(", "!!!~``"],
            "whitespace": ["\t", "\n", " "],
            "jiddisch": ["רעכט צו לינקס", "שאָסיי 61", "פּיצאַ איז אָנגענעם"],
            "arabic": ["بوب ديلان", "باتي فالنتين", "السيد الدف الرجل"],
            "playing_cards": ["🂶", "🃁", "🂻"],
        }
    )

    typeset = CompleteSet()
    new_df = cast_frame(df, typeset)
    assert new_df["digits"].iloc[1] - 3 == 121220
    assert new_df["latin"].iloc[1] + "1" == "apple1"


def test_type_cast_series():
    string_series = pd.Series(["(12.0+10.0j)", "(-4.0+6.2j)", "(8.0+2.0j)"])

    typeset = StandardSet()
    new_series = cast_series(string_series, typeset)
    assert new_series.iloc[1].real == -4.0


def test_type_detect_frame():
    # Create a DataFrame with various string columns
    df = pd.DataFrame(
        {
            "latin": ["orange", "apple", "pear"],
            "cyrillic": ["Кириллица", "гласность", "демократија"],
            "mixed": ["Кириллица", "soep", "демократија"],
            "burmese": ["ရေကြီးခြင်း", "စက်သင်ယူမှု", "ဉာဏ်ရည်တု"],
            "digits": ["01234", "121223", "12312"],
            "specials": ["$", "%^&*(", "!!!~``"],
            "whitespace": ["\t", "\n", " "],
            "jiddisch": ["רעכט צו לינקס", "שאָסיי 61", "פּיצאַ איז אָנגענעם"],
            "arabic": ["بوب ديلان", "باتي فالنتين", "السيد الدف الرجل"],
            "playing_cards": ["🂶", "🃁", "🂻"],
        }
    )

    # Initialize the typeset
    typeset = CompleteSet()

    # Infer the column type
    types = detect_frame_type(df, typeset)
    assert types == {
        "latin": String,
        "cyrillic": String,
        "mixed": String,
        "burmese": String,
        "digits": String,
        "specials": String,
        "whitespace": String,
        "jiddisch": String,
        "arabic": String,
        "playing_cards": String,
    }


def test_type_detect_series():
    datetime_series = pd.Series(
        [
            pd.datetime(2010, 1, 1),
            pd.datetime(2010, 8, 2),
            pd.datetime(2011, 2, 1),
            np.datetime64("NaT"),
        ]
    )

    typeset = StandardSet()
    detected_type = detect_series_type(datetime_series, typeset)
    assert detected_type == DateTime
