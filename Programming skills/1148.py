import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask_author_viewer = (views.loc[:,"author_id"] == views.loc[:,"viewer_id"])
    view = views.sort_values(by="author_id").loc[mask_author_viewer,"author_id"].drop_duplicates(ignore_index=True)
    return pd.DataFrame(view).rename(columns={"author_id":"id"})

data_input = { 'article_id': [1, 1, 2, 2, 4, 3, 3], 'author_id': [3, 3, 7, 7, 7, 4, 4], 'viewer_id': [5, 6, 7, 6, 1, 4, 4], 'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21'] } 
# Creating DataFrame 
df_input = pd.DataFrame(data_input)

data_output = { 'id': [4, 7] }
df_output = pd.DataFrame(data_output)
print(df_output)

assert article_views(df_input).equals(df_output)