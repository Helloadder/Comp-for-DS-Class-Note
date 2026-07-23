"""A tiny test suite for simple_eda."""

import pandas as pd

import simple_eda as eda


def _tiny_df():
    return pd.DataFrame(
        {
            "name": ["Ana", "Bo", None],
            "age": [25, None, 31],
        }
    )


def test_summarize_shape_and_names():
    df = _tiny_df()
    result = eda.summarize(df)
    assert result["rows"] == 3
    assert result["columns"] == 2
    assert result["names"] == ["name", "age"]
    assert set(result["dtypes"]) == {"name", "age"}


def test_missing_counts_sorted_descending():
    df = _tiny_df()
    counts = eda.missing(df)
    # One null in each column here.
    assert counts["name"] == 1
    assert counts["age"] == 1
    # Result is sorted descending, so values never increase.
    assert list(counts) == sorted(counts, reverse=True)


def test_numeric_columns():
    df = pd.DataFrame({"name": ["A"], "age": [10]})
    cols = eda.numeric_columns(df)
    assert cols == ["age"]


def test_categorical_columns():
    df = pd.DataFrame({"name": ["A"], "age": [10]})
    cols = eda.categorical_columns(df)
    assert cols == ["name"]


def test_public_api():
    assert eda.__all__ == [
        "summarize",
        "missing",
        "numeric_columns",
        "categorical_columns",
    ]
