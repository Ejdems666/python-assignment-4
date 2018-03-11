import csv


def get_csv_reader(f):
    f.seek(0)
    reader = csv.reader(f, delimiter=",")
    next(reader)
    return reader
