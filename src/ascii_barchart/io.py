import csv


def load_rows(path):
    with open(path, encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    return rows
