import operator

from common_functions import get_csv_reader


def run(f):
    processed_data = get_teams_with_cumulative_player_worth(f)
    sorted_data = sorted(processed_data.items(), key=operator.itemgetter(1), reverse=True)

    richest_teams = sorted_data[:3]
    print("Richest teams:")
    print_teams_in_order(richest_teams)

    poorest_teams = sorted_data[len(sorted_data) - 3:]
    print("\nPoorest teams:")
    print_teams_in_order(poorest_teams)


def get_teams_with_cumulative_player_worth(f):
    csv_reader = get_csv_reader(f)
    result_data = {}
    for row in csv_reader:
        team_name = row[3]
        if team_name != "":
            player_worth = float(row[16])
            result_data.setdefault(team_name, 0)
            result_data[team_name] += player_worth
    return result_data


def print_teams_in_order(data):
    i = 1
    base_indentation = 40
    for team_name, worth in data:
        calculated_indentation = base_indentation - len(team_name)
        print(i, team_name, calculated_indentation * ".", format(worth, ','), 'Eur')
        i += 1
