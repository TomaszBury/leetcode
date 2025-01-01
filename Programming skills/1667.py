import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.loc[:,"name"] = users.loc[:,"name"].str.capitalize()
    users.sort_values(by="user_id", inplace=True)
    return users