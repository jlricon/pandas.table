from pandastable.core import PandasTable
import pandas as pd


def test_creation():
    dt = pd.DataFrame({"a": [1, 2], "b": [2, 3]})
    dt2 = PandasTable(dt)
    assert dt.equals(dt2)
