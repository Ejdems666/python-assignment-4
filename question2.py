from common_functions import get_csv_reader


def run(f):
    ethnicity_sums = sum_nationality(f)
    result = find_biggest_sum_in_dict(ethnicity_sums)
    print("The nationality with the most players was: \"" + result["name"].lower().capitalize() +
          "\" with a total count of " + str(result["sum"]) + " players.")


def sum_nationality(f):
    csv_data = get_csv_reader(f)
    player_counter = {}
    for row in csv_data:
        player_counter.setdefault(row[14], 0)
        player_counter[row[14]] += 1
    return player_counter


def find_biggest_sum_in_dict(data):
    biggest_sum = 0
    biggest_key = ''
    for key, count in data.items():
        if biggest_sum < count:
            biggest_key = key
            biggest_sum = count
    return {"name": biggest_key, "sum": biggest_sum}
