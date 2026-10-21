import csv


def load_rows(path):
    with open(path, encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    return rows

if __name__ == "__main__":
    rows = load_rows("data/points.csv")

    for row in rows:
        print(row)