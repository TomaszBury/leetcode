import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df_sorted = activity.sort_values(by='event_date')
    df_no_duplicates = df_sorted.drop_duplicates(subset='player_id', keep="first")
    df_no_duplicates.rename(columns={'event_date': 'first_login'}, inplace=True)

    return df_no_duplicates.loc[:,["player_id","first_login"]]


data = {
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
    'games_played': [5, 6, 1, 0, 5]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print(game_analysis(df))