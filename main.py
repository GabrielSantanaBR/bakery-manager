from excel_manager import load_excel

REQUIRED_SHEETS = [
    "Produtos",
    "Cafeteria 1",
    "Cafeteria 2",
    "Cafeteria 3",
    "Resumo Mensal"
]

def main():

    sheets = load_excel()

    print("\nWorkbook loaded successfully!\n")

    for sheet in REQUIRED_SHEETS:
        if sheet in sheets:
            print(f"✓ {sheet}")
        else:
            print(f"✗ Missing sheet: {sheet}")

if __name__ == "__main__":
    main()
