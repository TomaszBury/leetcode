import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby(['actor_id', 'director_id']).size().reset_index(name='count')

    result = grouped[grouped['count'] >= 3]

    final_result = result[['actor_id', 'director_id']]

    return final_result


df = pd.DataFrame({
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6]
})

print(actors_and_directors(df))
