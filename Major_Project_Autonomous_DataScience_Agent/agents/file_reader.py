import pandas as pd
from pathlib import Path


class FileReaderAgent:

    def load_file(self, uploaded_file):

        extension = Path(uploaded_file.name).suffix.lower()

        if extension == ".csv":
            df = pd.read_csv(uploaded_file)

        elif extension in [".xlsx", ".xls"]:
            df = pd.read_excel(uploaded_file)

        elif extension == ".json":
            df = pd.read_json(uploaded_file)

        else:
            raise ValueError("Unsupported file format")

        return df