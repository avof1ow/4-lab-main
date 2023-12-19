import datetime

import pandas as pd


def inpute_date(year: int, month: int, day: int, path: str) -> tuple[str, int]:
    """_summary_
        Принимаются день, месяц и год
        возвращается курс по заданной дате
    Args:
        year (int): год нужного курса
        month (int): месяц нужного курса
        day (int): день нужного курса

    Returns:
        tuple[str, int]: возвращает кортеж с датой и курсом рубля
    """
    df = pd.read_csv(path, usecols=["rouble", "date"])
    date = datetime.date(year, month, day)
    rouble = df[df["date"] == str(date)]["rouble"].values[0]
    return (str(date), rouble)


if __name__ == "__main__":
    print(inpute_date(2022, 12, 27, "CSV/dollar_course.csv"))
