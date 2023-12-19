import pandas as pd


def week(path: str) -> None:
    """_summary_
    Принимается таблица, после чего сортируется в разные файлы по неделям
    """
    df = pd.read_csv(path, usecols=["rouble", "date"])
    for i in range(7, len(df), 7):
        data = df.iloc[i - 7 : i]
        data.index = pd.RangeIndex(start=0, stop=len(data), step=1)
        data.to_csv(
            "CSV/" + data["date"].values[0] + "_" + data["date"].values[-1] + ".csv"
        )


if __name__ == "__main__":
    week("CSV/dollar_course.csv")
