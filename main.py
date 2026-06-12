from excel_manager import load_excel

def main():

    sheets = load_excel()

    print("\nSheets found:\n")

    for sheet in sheets:
        print(sheet)

if __name__ == "__main__":
    main()
