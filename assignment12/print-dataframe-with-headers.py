import pandas as pd

class DFPlus(pd.DataFrame):

    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        total_rows = len(self)
        for start in range(0, total_rows, 10):
            end = min(start + 10, total_rows)
            print(self.columns.to_list())
            print(self.iloc[start:end])
            print()


if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()