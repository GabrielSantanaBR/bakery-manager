import pandas as pd

FILE_PATH = "database/Bakery_Manager.xlsx"


def load_excel():

    sheets = pd.read_excel(
        FILE_PATH,
        sheet_name=None
    )

    return sheets