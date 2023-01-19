import glob

from mycsv import csvparser


def main():
    try:
        files = glob.glob("data/*.csv")
        for item in files:
            print("\n\n")
            print(f"opening file: {item}")
            with open(item) as file:
                while True:
                    row = csvparser.read_row(file)

                    if row is None:
                        print('<EOF>')
                        break
                    else:
                        print(f'    {row[0]} - {row[1]} - {row[2]} - {row[3]}')

    except Exception as e:
        print(f'Error reading CSV file - {str(e)}')
        exit(1)


if __name__ == '__main__':
    main()
