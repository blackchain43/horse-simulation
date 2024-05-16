import pandas as pd


def display_results(race_result: list[pd.DataFrame], num_horses: int = 3) -> None:
    # Merge the DataFrames
    merged_df = pd.concat([df for df in race_result], axis=1)
    # Select only 'round' and 'round_points' columns
    selected_df = merged_df[["round_points"]]
    selected_df.columns = [f"Player {i + 1}" for i in range(num_horses)]
    transposed_df = selected_df.transpose()
    print(transposed_df)
