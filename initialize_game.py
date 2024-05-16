import random
import pandas as pd

def get_map_config(file_path: str) -> dict:
    result = {}
    df = pd.read_csv(file_path, header=None, names=["key", "value"])
    map_config = df[df["key"].str.startswith("num_")]
    map_config_dict = map_config.to_dict("list")
    for idx, key in enumerate(map_config_dict['key']):
        result[key] = int(map_config_dict['value'][idx])
    return result


# Function to get rows without 'vip_' prefix
def get_non_vip_rows(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, header=None, names=["key", "value"])
    non_vip_df = df[~(df["key"].str.startswith("vip_")) & ~(df["key"].str.startswith("num_"))]
    return non_vip_df


# Function to get rows with 'vip_' prefix
def get_vip_rows(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, header=None, names=["key", "value"])
    vip_df = df[df["key"].str.startswith("vip_") & ~(df["key"].str.startswith("num_"))].copy()
    vip_df["key"] = vip_df["key"].str.replace("vip_", "", regex=False)
    return vip_df


def process_load_game(df: pd.DataFrame) -> dict:
    game_info = {}
    for index, row in df.iterrows():
        key, value = row["key"], row["value"]
        game_info[key] = int(value)
    return game_info


# Function to load normal game info
def load_normal_game_info(file_path: str) -> dict:
    df = get_non_vip_rows(file_path)
    return process_load_game(df)


# Function to load VIP game info
def load_vip_game_info(file_path: str) -> tuple[dict, list[int]]:
    df = get_vip_rows(file_path)

    # Handle the special case where key is 'players'
    players_row = df[df["key"] == "players"]
    players_value = []
    if not players_row.empty:
        players_value = [int(x) for x in players_row.iloc[0]["value"].split(":")]
        df = df[df["key"] != "players"]

    game_info = process_load_game(df)

    return game_info, players_value


def initialize_map(num_cells: int, game_info: dict) -> dict:
    game_map = {}

    for cell in range(1, num_cells + 1):
        # select condition type of that cell, ex: normal
        condition = random.choice(list(game_info.keys()))
        game_map[cell] = {
            "condition": condition,
            "reward": game_info[condition],
        }
    return game_map
