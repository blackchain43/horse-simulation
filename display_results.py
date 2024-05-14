import pandas as pd

def display_results(race_result: list[dict], num_horses: int) -> None:
    display_data = {}
    for horse in range(num_horses):
        display_data[f"Player {horse + 1}"] = [result["round_points"][horse] for result in race_result]
        display_data[f"Player {horse + 1}"].insert(0, 0)
    df = pd.DataFrame(display_data)
    df = df.transpose()
    print(df)
