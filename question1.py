from common_functions import get_csv_reader, print_results_in_order


def run(f):
    processed_data = get_teams_with_cumulative_player_worth(f)

    def get_worth(x): return processed_data[x]

    sorted_names = sorted(processed_data.keys(), key=get_worth, reverse=True)

    richest_team_names = sorted_names[:3]
    print('Richest teams:')
    print_results_in_order(richest_team_names, get_worth)

    poorest_team_names = sorted_names[len(sorted_names) - 3:]
    print('\nPoorest teams:')
    print_results_in_order(poorest_team_names, get_worth)


def get_teams_with_cumulative_player_worth(f):
    csv_reader = get_csv_reader(f)
    result_data = {}
    for row in csv_reader:
        team_name = row[3]
        if team_name != '':
            player_worth = float(row[16])
            result_data.setdefault(team_name, 0)
            result_data[team_name] += player_worth
    return result_data
