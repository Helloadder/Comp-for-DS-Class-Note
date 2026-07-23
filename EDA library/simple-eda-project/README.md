# simple-eda-dzhu9

Tiny EDA helper for pandas. It gives you a handful of boring, useful
functions for a first look at a `DataFrame` — no dashboards, no custom
classes, just plain dicts, lists, and a pandas `Series`.

## Install

```bash
pip install simple-eda-dzhu9
```

Or, from a local checkout (editable / development install):

```bash
# run from the folder that contains pyproject.toml
python -m pip install -e .
```

## Use

```python
import pandas as pd
import simple_eda as eda

df = pd.DataFrame({
    "name": ["Ana", "Bo", None],
    "age": [25, None, 31],
})

print(eda.summarize(df))
# {'rows': 3, 'columns': 2, 'names': ['name', 'age'],
#  'dtypes': {'name': 'object', 'age': 'float64'}}

print(eda.missing(df))
# age     1
# name    1
# dtype: int64

print(eda.numeric_columns(df))      # ['age']
print(eda.categorical_columns(df))  # ['name']
```

## API

| Function | Returns | What it does |
| --- | --- | --- |
| `summarize(df)` | `dict` | Rows, columns, column names, and dtypes. |
| `missing(df)` | `pandas.Series` | Null counts per column, sorted descending. |
| `numeric_columns(df)` | `list[str]` | Names of numeric columns. |
| `categorical_columns(df)` | `list[str]` | Names of object/category columns. |

## Notes

- Input: pandas `DataFrame` only (not Polars, Spark, Dask, or Arrow yet).
- Output: plain objects (dicts, lists, ints, strings, pandas `Series`).
- Functions never modify the DataFrame in place.

This is a `0.1.0` release: the first working version — installable and
understandable, not complete.

## License

MIT — see [LICENSE](LICENSE).
