def average_value1_by_type(rows):
    sums = {}
    counts = {}

    for row in rows:
        typ = row["type"]
        value = float(row["value1"])

        sums[typ] = sums.get(typ, 0) + value
        counts[typ] = counts.get(typ, 0) + 1

    averages = {}

    for typ in sums:
        averages[typ] = sums[typ] / counts[typ]

    return averages
