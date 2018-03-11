from common_functions import get_csv_reader, print_results_in_order


def run(f):
    processed_data = get_players_with_release_and_worth_diff(f)
    sorted_names = sorted(processed_data.keys(), key=lambda x: processed_data[x]['worth'], reverse=True)
    top_10_player_names = sorted_names[:10]
    print_results_in_order(top_10_player_names, lambda x: (processed_data[x]['difference']))


def get_players_with_release_and_worth_diff(f):
    csv_reader = get_csv_reader(f)
    processed_data = {}
    for row in csv_reader:
        release_clause = row[18]
        if release_clause != '':
            player_name = row[2]
            worth = float(row[16])
            release_clause = float(release_clause)
            processed_data.setdefault(player_name, {})
            processed_data[player_name] = {'worth': worth, 'difference': release_clause - worth}
    return processed_data