import math
from typing import Any, Generator

import pandas as pd


def next(df: pd.DataFrame) -> Generator[Any, Any, None]:
    """_summary_
        Принимается таблица с данными,
        создается генератор,
        пропускающий пустые значения курса
    Args:
        df (pd.DataFrame): принимается таблица с данными

    Yields:
        Generator[Any, Any, None]: возвращается значение генератора
    """
    for i in df.values:
        rouble = i[0]
        if not math.isnan(rouble):
            yield rouble


if __name__ == "__main__":
    df = pd.read_csv("CSV/dollar_course.csv", usecols=["rouble", "date"])
    for i in next(df):
        print(i)
