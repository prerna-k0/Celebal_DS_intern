import pandas as pd
from pandas.api.types import is_numeric_dtype


class DataCleaner:

    def clean(self, df):

        cleaned_df = df.copy()

        cleaned_df = cleaned_df.drop_duplicates()

        for column in cleaned_df.columns:

            # Try converting object columns to numeric where possible
            if cleaned_df[column].dtype == "object":
                converted = pd.to_numeric(cleaned_df[column], errors="ignore")
                cleaned_df[column] = converted

            if is_numeric_dtype(cleaned_df[column]):
                median = cleaned_df[column].median(skipna=True)
                cleaned_df[column] = cleaned_df[column].fillna(median)
            else:
                mode = cleaned_df[column].mode(dropna=True)
                if not mode.empty:
                    cleaned_df[column] = cleaned_df[column].fillna(mode.iloc[0])

        return cleaned_df