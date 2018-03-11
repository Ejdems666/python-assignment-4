import csv


def get_csv_reader(f):
    f.seek(0)
    reader = csv.reader(f, delimiter=',')
    next(reader)
    return reader


def print_results_in_order(data, value_getter):
    i = 1
    for key in data:
        base_indentation = 40
        calculated_indentation = base_indentation - (len(key) + len(str(i)))
        print(str(i)+'.',
              key,
              calculated_indentation * '.',
              format(value_getter(key), ','),
              'Eur')
        i += 1
