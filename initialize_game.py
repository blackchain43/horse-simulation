import random
import pandas as pd


def load_game_info(file_path: str) -> tuple[dict, list[int]]:
    game_info = {}
    vip_players = []
    file_data = pd.read_csv(file_path, header=None, names=["key", "value"])

    for index, row in file_data.iterrows():
        key, value = row["key"], row["value"]
        match key:
            case "vip_players":
                vip_players = [int(x) for x in value.split(":")]
            case _:
                condition, reward = key, int(value)
                game_info[condition] = reward
    return game_info, vip_players


def initialize_map(num_cells: int, game_info: dict) -> dict:
    game_map = {}
    vip_conditions = {
        key[4:]: value for key, value in game_info.items() if key.startswith("vip_")
    }
    regular_conditions = {
        key: value for key, value in game_info.items() if not key.startswith("vip_")
    }

    for cell in range(1, num_cells + 1):
        # select condition type of that cell, ex: normal
        condition = random.choice(list(regular_conditions.keys()))
        vip_reward = vip_conditions.get(condition, "vip_normal")

        game_map[cell] = {
            "condition": condition,
            "reward": regular_conditions[condition],
            "vip_reward": vip_reward,
        }
    return game_map
