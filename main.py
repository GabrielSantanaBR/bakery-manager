from excel_manager import load_excel, validate_structure


def main() -> None:
    sheets = load_excel()
    missing = validate_structure(sheets)

    print("Pricing & Sales Manager — public demo")
    print(f"Loaded {len(sheets)} worksheets.")

    if missing:
        print("\nMissing required worksheets:")
        for sheet in missing:
            print(f"  - {sheet}")
        raise SystemExit(1)

    print("\nWorkbook structure: OK")
    print("Available modules:")
    for sheet in ("Ingredients", "Recipes", "Pricing", "Sales", "Dashboard"):
        rows = len(sheets[sheet].dropna(how="all"))
        print(f"  ✓ {sheet}: {rows} non-empty rows")


if __name__ == "__main__":
    main()
