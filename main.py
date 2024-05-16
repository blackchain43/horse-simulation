from initialize_game import initialize_map, load_normal_game_info, load_vip_game_info
from game_simulation import race_normal_map, race_vip_map
from display_results import display_results
import sys

NUM_CELLS = 100
NUM_ROUNDS = 10
NUM_HORSES = 3


def script_a():
    # Load game info from CSV
    game_info = load_normal_game_info("game_info.csv")
    # Init game map
    game_map = initialize_map(NUM_CELLS, game_info)
    # Simulate race
    race_result = race_normal_map(game_map, NUM_ROUNDS, NUM_HORSES)
    # Display result
    display_results(race_result)


def script_b():
    # Load game info from CSV
    game_info = load_normal_game_info("game_info.csv")
    # Init game map
    game_map = initialize_map(NUM_CELLS, game_info)
    # Simulate race
    first_10_rounds_result = race_normal_map(game_map, NUM_ROUNDS, NUM_HORSES)


def script_c():
    # Load game info from CSV
    vip_game_info, vip_players = load_vip_game_info("game_info.csv")
    normal_game_info = load_normal_game_info("game_info.csv")
    # Init game map
    vip_game_map = initialize_map(NUM_CELLS, vip_game_info)
    normal_game_map = initialize_map(NUM_CELLS, normal_game_info)
    # Simulate race
    race_result = race_vip_map(
        normal_game_map, vip_game_map, NUM_ROUNDS, vip_players, NUM_HORSES
    )
    # Display result
    display_results(race_result)


def main(script_name: str):
    if script_name == "script_a":
        script_a()
    elif script_name == "script_b":
        script_b()
    elif script_name == "script_c":
        script_c()
    else:
        raise ValueError(f"Invalid script name: {script_name}")


def assign_initial_positions(last_round_results):
    print(f"Last round results {last_round_results}")
    # Copying the original list to keep track of the original indices
    indexed_results = list(enumerate(last_round_results))
    # Sorting the list based on the scores (second element of the tuple), descending
    indexed_results.sort(key=lambda x: x[1], reverse=True)

    # Creating a new list for scores, initialized with zeros
    scores = [0] * len(last_round_results)

    # Assigning scores according to the sorted values
    scores[indexed_results[0][0]] = 2  # Max value gets a score of 2
    scores[indexed_results[1][0]] = 1  # Second highest value gets a score of 1
    scores[indexed_results[2][0]] = 0  # Lowest value gets a score of 3

    return scores


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <script_name>")
        sys.exit(1)
    main(sys.argv[1])
