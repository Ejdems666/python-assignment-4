from common_functions import get_csv_reader


def run(f):
    avg_value = avg_of_row(f, 16)
    avg_wage = avg_of_row(f, 17)
    print('The average difference between value and wage was: "' + str(round(avg_value - avg_wage, 2)) +
          '" with average value being: ' + str(avg_value) + ' and average wage being: ' + str(avg_wage) + '.')


def avg_of_row(f, row_num):
    csv_data = get_csv_reader(f)
    total_value = 0
    counter = 0
    for row in csv_data:
        total_value += float(row[row_num])
        counter += 1
    return round(total_value / counter, 2)
