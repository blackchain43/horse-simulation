from initialize_game import initialize_map, load_game_info
from game_simulation import simulate_race
from display_results import display_results


def main():
    # Load game info from CSV
    game_info, num_cells, rounds, num_horses, vip_players = load_game_info("game_info.csv")
    # Initialize game map
    game_map = initialize_map(num_cells, game_info)

    # Simulate race
    race_result = simulate_race(game_map, rounds, num_horses, vip_players)

    # Display results
    display_results(race_result, num_horses)


if __name__ == "__main__":
    # This block will only execute if the script is run directly, not imported as a module
    main()
