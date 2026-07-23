"""simple_eda — a tiny EDA helper for pandas.

Import it and call the helpers directly on a pandas DataFrame::

    import pandas as pd
    import simple_eda as eda

    df = pd.read_csv("data.csv")
    eda.summarize(df)
    eda.missing(df)
"""

from .core import (
    categorical_columns,
    missing,
    numeric_columns,
    summarize,
)

__version__ = "0.1.0"

__all__ = [
    "summarize",
    "missing",
    "numeric_columns",
    "categorical_columns",
]
