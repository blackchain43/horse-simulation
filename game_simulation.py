import random
import pandas as pd


def find_normal_indices(total_players, vip_indices):
    all_indices = set(range(total_players))
    vip_indices_set = set(vip_indices)
    normal_indices = list(all_indices - vip_indices_set)
    return normal_indices


def simulate_race(
    game_map: dict,
    num_rounds: int,
    initial_positions: int = 0,
) -> pd.DataFrame:
    horse_points = 0
    horse_positions = [initial_positions] * num_rounds
    round_points = [0] * num_rounds

    race_result = [
        {
            "round": 0,
            "horse_accumulated_points": 0,
            "round_points": 0,
        }
    ]

    for round_num in range(num_rounds):
        step = random.randint(1, 5)  # Simulate 1 to 5 steps
        horse_positions[round_num] += step
        # Get the condition at the current position
        cell_info = game_map.get(
            horse_positions[round_num],
            {"condition": "normal", "reward": 1},
        )

        # Reward based on condition
        round_points[round_num] = cell_info["reward"]

        # Update points based on the condition
        horse_points += cell_info["reward"]
        if round_num + 1 < num_rounds:
            horse_positions[round_num + 1] = horse_positions[round_num]

        race_result.append(
            {
                "round": round_num + 1,
                "horse_accumulated_points": horse_points,
                "round_points": round_points[round_num],
            }
        )

    return pd.DataFrame(race_result)


def race_normal_map(
    game_map: dict,
    num_rounds: int,
    num_horses: int = 3,
) -> list[pd.DataFrame]:
    return [simulate_race(game_map, num_rounds) for _ in range(num_horses)]


def race_normal_map_with_init_positions(
    game_map: dict,
    num_rounds: int,
    initial_positions: list[int],
    num_horses: int = 3,
):
    if len(initial_positions) != num_horses:
        raise ValueError(
            "Number of initial positions must be equal to the number of horses"
        )
    return [
        simulate_race(game_map, num_rounds, initial_position)
        for initial_position in initial_positions
    ]


def race_vip_map(
    normal_game_map: dict,
    vip_game_map: dict,
    num_rounds: int,
    vip_players: list[int],
    num_horses: int = 3,
) -> list[pd.DataFrame]:
    if len(vip_players) > num_horses:
        raise ValueError(
            "Number of VIP players cannot be greater than the number of horses"
        )
    normal_map_result = race_normal_map(
        normal_game_map, num_rounds, num_horses - len(vip_players)
    )

    vip_map_result = race_normal_map(vip_game_map, num_rounds, len(vip_players))

    # arrange the results based on the index of player in vip_players list
    vip_indices = [player - 1 for player in vip_players]
    normal_indices = find_normal_indices(num_horses, vip_indices)
    print(f"vip_indices {vip_indices} - normal_indices {normal_indices}")

    final_result = [[] for _ in range(num_horses)]

    # Assign VIP players' results to the final_result
    for idx, vip_index in enumerate(vip_indices):
        final_result[vip_index] = vip_map_result[idx]

    # Assign normal players' results to the final_result
    for idx, normal_index in enumerate(normal_indices):
        final_result[normal_index] = normal_map_result[idx]

    return final_result
