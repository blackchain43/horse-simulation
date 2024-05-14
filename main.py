from initialize_game import initialize_map, load_game_info
from game_simulation import simulate_race
from display_results import display_results

NUM_CELLS = 100
NUM_ROUNDS = 10
NUM_HORSES = 3

def main():
    # Load game info from CSV
    game_info, vip_players = load_game_info("game_info.csv")
    # Initialize game map
    game_map = initialize_map(NUM_CELLS, game_info)

    # Simulate race
    first_10_rounds_race_result = simulate_race(game_map, NUM_ROUNDS, NUM_HORSES, vip_players)

    race_result = simulate_race(game_map, NUM_ROUNDS, NUM_HORSES, vip_players, assign_initial_positions(first_10_rounds_race_result[-1]["horse_accumulated_points"]))
    # Display results
    display_results(race_result, NUM_HORSES)

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
    # This block will only execute if the script is run directly, not imported as a module
    main()
