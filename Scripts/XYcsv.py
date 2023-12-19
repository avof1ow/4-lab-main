import pandas as pd


def xy(path: str) -> None:
    """_summary_
    принимается таблица, после чего делится на 2 таблицы, содержащие дату одна и курс другая
    """
    df = pd.read_csv(path, usecols=["rouble", "date"])
    df["date"].to_csv("CSV/X.csv")
    df["rouble"].to_csv("CSV/Y.csv")


if __name__ == "__main__":
    xy("CSV/dollar_course.csv")
