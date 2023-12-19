import math

import pandas as pd


class Iterator:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.index = 0
        self.limit = len(df)

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < self.limit:
            course = self.df[self.df.index == self.index].values
            rouble = course[0][0]
            self.index += 1
            if math.isnan(rouble):
                continue
            return rouble

        else:
            raise StopIteration


if __name__ == "__main__":
    df = pd.read_csv("CSV/dollar_course.csv", usecols=["rouble", "date"])
    iterator = Iterator(df)
    for i in iterator:
        print(i)
