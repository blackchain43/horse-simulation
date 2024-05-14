import random


def simulate_race(
    game_map: dict,
    num_rounds: int,
    num_horses: int,
    vip_players: list[int],
    # initial_positions: list[int] = None,
) -> list[dict]:
    horse_points = [0] * num_horses
    horse_positions = [[0] * num_horses for _ in range(num_rounds)]
    # horse_positions = [[initial_positions[horse] if initial_positions else 0 for horse in range(num_horses)] for _ in range(num_rounds)]
    round_points = [[0] * num_horses for _ in range(num_rounds)]

    race_result = []

    for round_num in range(num_rounds):
        round_positions = []
        round_acc_points = []
        for horse in range(num_horses):
            # Simulate movement using random steps
            step = random.randint(1, 5)  # Simulate 1 to 5 steps
            horse_positions[round_num][horse] += step

            # Get the condition at the current position
            cell_info = game_map.get(
                horse_positions[round_num][horse],
                {"condition": "normal", "reward": 1, "vip_reward": 1},
            )
            # Reward based on condition
            round_points[round_num][horse] = cell_info["reward"]

            # Update points based on the condition
            if horse + 1 in vip_players:
                horse_points[horse] += cell_info["vip_reward"]
            else:
                horse_points[horse] += cell_info["reward"]

            # Update position of the horse in this round
            round_positions.append(horse_positions[round_num][horse])
            round_acc_points.append(horse_points[horse])

            print(
                f"Round {round_num + 1}, Horse {horse + 1}, Position {horse_positions[round_num][horse]}, Condition: {cell_info['condition']}, Round Points: {round_points[round_num][horse]}, Total Points: {horse_points[horse]}"
            )
        if round_num + 1 < num_rounds:
            horse_positions[round_num + 1] = horse_positions[round_num]
        race_result.append(
            {
                "round": round_num + 1,
                "horse_accumulated_points": round_acc_points,
                "positions": round_positions,
                "round_points": round_points[round_num],
            }
        )

    return race_result
