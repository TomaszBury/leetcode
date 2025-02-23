import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return_columns:list[str] = ['id','movie','description','rating']

    mask_boring:pd.Series = (cinema.loc[:,"description"] != "boring")

    cinema = cinema.loc[mask_boring,:].sort_values(by=["rating"],ascending=False)

    cinema.loc[:,"is_odd"] = cinema.loc[:,"id"] % 2 != 0

    mask_odd_id:pd.Series = (cinema.loc[:,"is_odd"] == True)
    
    result_df:pd.DataFrame = cinema.loc[mask_odd_id,return_columns]

    if not result_df.empty:
        return result_df
    else:
        return pd.DataFrame({'id': [],'movie': [],'description': [],'rating': []})

cinema_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'],
    'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'],
    'rating': [8.9, 8.5, 6.2, 8.6, 9.1]
})

print(not_boring_movies(cinema_df))