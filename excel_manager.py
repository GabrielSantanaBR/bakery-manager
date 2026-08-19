from pathlib import Path
from typing import Dict

import pandas as pd


DEFAULT_FILE_PATH = Path("demo") / "small-business-pricing-manager-demo.xlsx"
REQUIRED_SHEETS = {
    "Config",
    "Ingredients",
    "Recipes",
    "Pricing",
    "Sales",
    "Dashboard",
}


def load_excel(file_path: Path | str = DEFAULT_FILE_PATH) -> Dict[str, pd.DataFrame]:
    """Load every worksheet from the public portfolio workbook."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Workbook not found: {path}")

    return pd.read_excel(path, sheet_name=None)


def validate_structure(sheets: Dict[str, pd.DataFrame]) -> list[str]:
    """Return the names of required worksheets that are missing."""
    return sorted(REQUIRED_SHEETS.difference(sheets))
