import random
import csv

DEFAULT_NUM_CELLS = 100
DEFAULT_ROUNDS = 10
DEFAULT_NUM_HORSES = 3


def load_game_info(file_path: str) -> tuple[dict, int, int, int, list[int]]:
    game_info = {}
    vip_players = []
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key, value = row[0], row[1]
            if key == "num_cells":
                DEFAULT_NUM_CELLS = int(value)
            elif key == "rounds":
                DEFAULT_ROUNDS = int(value)
            elif key == "num_horses":
                DEFAULT_NUM_HORSES = int(value)
            elif key == "vip_players":
                vip_players = [int(x) for x in value.split(",")]
            else:
                condition, reward = key, int(value)
                game_info[condition] = reward
    return game_info, DEFAULT_NUM_CELLS, DEFAULT_ROUNDS, DEFAULT_NUM_HORSES, vip_players


def initialize_map(num_cells: int, game_info: int) -> dict:
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
