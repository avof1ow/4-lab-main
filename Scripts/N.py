import pandas as pd


def N(path: str) -> None:
    """_summary_
    Сперва выбираются все даты из таблицы,
    после чего таблица делится на новые таблицы,
    отсортированные по году
    """
    df = pd.read_csv(path, usecols=["rouble", "date"])
    year_set = set(year[:4] for year in df["date"])

    for year in year_set:
        data = df[(df["date"] >= f"{year}-01-01") & (df["date"] <= f"{year}-12-31")]
        data.index = pd.RangeIndex(start=0, stop=len(data), step=1)
        data.to_csv(
            "CSV/" + data["date"].values[0] + "_" + data["date"].values[-1] + ".csv"
        )


if __name__ == "__main__":
    N("CSV/dollar_course.csv")
