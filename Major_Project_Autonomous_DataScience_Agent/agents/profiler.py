import pandas as pd


class DataProfiler:

    def profile(self, df):

        profile = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": df.isnull().sum(),
            "duplicate_rows": df.duplicated().sum(),
            "data_types": df.dtypes,
            "summary": df.describe(include="all")
        }

        return profile