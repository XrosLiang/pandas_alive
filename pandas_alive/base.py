import pandas as pd
from typing import List


def load_dataset(name: str = "covid19") -> pd.DataFrame:
    """ Returns a pandas DataFrame suitable for immediate use in `pandas-alive`

    Args:
        name (str, optional): Name of dataset to load. Either 'covid19' or 'urban_pop'. Defaults to 'covid19'.

    Returns:
        pd.DataFrame: Loaded DataFrame
    """

    return pd.read_csv(
        f"https://raw.githubusercontent.com/JackMcKew/pandas-alive/master/data/{name}.csv",
        index_col="date",
        parse_dates=["date"],
    )


def plot_animated_grid(children_plots: List):
    # TODO Implement multiple animated plots
    a = 0
