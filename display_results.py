def display_results(race_result: list[dict], num_horses: int) -> None:
    num_rounds = len(race_result)

    # Print rounds header
    rounds_header = "Round: " + ", ".join(
        str(result["round"]) for result in race_result
    )
    print(rounds_header)

    # Print points for each player
    for horse in range(num_horses):
        points_line = [result["round_points"][horse] for result in race_result]
        points_line.insert(0, 0)
        points_string = ", ".join(map(str, points_line))
        print(f"Player {horse + 1}: {points_string}")
