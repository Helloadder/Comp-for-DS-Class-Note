"""Core EDA helper functions for pandas DataFrames.

Each function does one small job and returns plain objects (dicts, lists,
or a pandas Series) so there are no custom classes to learn. None of these
functions modify the DataFrame in place.
"""

from __future__ import annotations

import pandas as pd


def summarize(df: pd.DataFrame) -> dict:
    """Return a small summary of a DataFrame's shape and columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to summarize.

    Returns
    -------
    dict
        A dictionary with the number of rows, the number of columns, the
        column names, and each column's dtype as a string.

    Examples
    --------
    >>> import pandas as pd
    >>> import simple_eda as eda
    >>> df = pd.DataFrame({"name": ["Ana", "Bo"], "age": [25, 31]})
    >>> eda.summarize(df)
    {'rows': 2, 'columns': 2, 'names': ['name', 'age'],
     'dtypes': {'name': 'object', 'age': 'int64'}}
    """
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "names": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
    }


def missing(df: pd.DataFrame) -> pd.Series:
    """Return the count of missing (null) values per column.

    The result is sorted from the most missing to the least, so the columns
    that need attention appear first.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to inspect.

    Returns
    -------
    pandas.Series
        Missing-value counts indexed by column name, sorted descending.

    Examples
    --------
    >>> import pandas as pd
    >>> import simple_eda as eda
    >>> df = pd.DataFrame({"name": ["Ana", None], "age": [None, 31]})
    >>> eda.missing(df)
    name    1
    age     1
    dtype: int64
    """
    counts = df.isna().sum()
    return counts.sort_values(ascending=False)


def numeric_columns(df: pd.DataFrame) -> list:
    """Return the names of the numeric columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to inspect.

    Returns
    -------
    list of str
        Column names whose dtype is numeric.

    Examples
    --------
    >>> import pandas as pd
    >>> import simple_eda as eda
    >>> df = pd.DataFrame({"name": ["A"], "age": [10]})
    >>> eda.numeric_columns(df)
    ['age']
    """
    sel = df.select_dtypes(include="number")
    return list(sel.columns)


def categorical_columns(df: pd.DataFrame) -> list:
    """Return the names of the categorical / text columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to inspect.

    Returns
    -------
    list of str
        Column names whose dtype is ``object`` or ``category``.

    Examples
    --------
    >>> import pandas as pd
    >>> import simple_eda as eda
    >>> df = pd.DataFrame({"name": ["A"], "age": [10]})
    >>> eda.categorical_columns(df)
    ['name']
    """
    sel = df.select_dtypes(include=["object", "category"])
    return list(sel.columns)
