from pathlib import Path
import pandas as pd

FILE_PATH = Path("database") /"Bakery_Manager.xlsx"


def load_excel():

    if not FILE_PATH.exists():
        raise FileNotFoundError(
            f"Excel file not found: {FILE_PATH}"
        )

    sheets = pd.read_excel(
        FILE_PATH,
        sheet_name=None
    )

    return sheets